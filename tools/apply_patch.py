#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""apply_patch.py — แก้ไฟล์ผ่านสคริปต์เท่านั้น (ตาม SOP)

บังคับ: ต้องระบุ md5 ของไฟล์เป้าหมายก่อนแก้ถ้าไม่ตรง = ปฏิเสธ ไม่แตะไฟล์

Usage:
  python3 tools/apply_patch.py --file <target> --expect-md5 <md5> --patch <change.diff> [--dry-run]
  cat change.diff | python3 tools/apply_patch.py --file <target> --expect-md5 <md5> [--dry-run]

diff ต้องเป็น unified diff ที่มีหัว --- / +++ ของไฟล์เป้าหมาย
Exit codes: 0 = สำเร็จ | 2 = ไม่พบไฟล์ | 3 = md5 ไม่ตรง | 4 = diff ว่าง/อ่านไม่ได้ | 5 = patch ล้มเหลว
"""
import argparse, hashlib, os, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser(
        description="Patch a file only after verifying its md5 (SOP-compliant).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__)
    ap.add_argument("--file", required=True, help="ไฟล์เป้าหมาย (path)")
    ap.add_argument("--expect-md5", required=True, dest="expect_md5",
                    help="md5 ที่คาดไว้ของไฟล์เป้าหมาย ก่อนแก้")
    ap.add_argument("--patch", help="ไฟล์ unified diff (ถ้าไม่ระบุ = อ่านจาก stdin)")
    ap.add_argument("--dry-run", action="store_true", help="ลองก่อน ไม่เขียนจริง")
    ap.add_argument("--update-manifest", action="store_true",
                    help="อัปเดต md5 ของไฟล์นี้ใน MANIFEST.md5 หลังแก้สำเร็จ")
    a = ap.parse_args()

    target = a.file
    if not os.path.isfile(target):
        print("ERROR: file not found: %s" % target, file=sys.stderr)
        return 2

    got = md5(target)
    if got.lower() != a.expect_md5.strip().lower():
        print("MD5 MISMATCH — ปฏิเสธการแก้ไข (ตาม SOP)", file=sys.stderr)
        print("  file   : %s" % target, file=sys.stderr)
        print("  expect : %s" % a.expect_md5.strip(), file=sys.stderr)
        print("  actual : %s" % got, file=sys.stderr)
        return 3

    if a.patch:
        try:
            data = open(a.patch, "rb").read()
        except OSError as e:
            print("ERROR: cannot read patch: %s" % e, file=sys.stderr)
            return 4
    else:
        data = sys.stdin.buffer.read()
    if not data.strip():
        print("ERROR: empty diff", file=sys.stderr)
        return 4

    # ใช้ absolute path + รัน patch ในโฟลเดอร์ของไฟล์เป้าหมาย
    target_abs = os.path.abspath(target)
    cmd = ["patch", "--forward", "--batch"]
    if a.dry_run:
        cmd.append("--dry-run")
    cmd.append(target_abs)
    print("$ " + " ".join(cmd) + "   < <diff>")
    p = subprocess.run(cmd, input=data, cwd=os.path.dirname(target_abs))
    if p.returncode != 0:
        print("PATCH FAILED (exit %d)" % p.returncode, file=sys.stderr)
        return 5

    if a.dry_run:
        print("DRY-RUN OK — ยังไม่มีการเปลี่ยนแปลงไฟล์")
        return 0

    new = md5(target)
    print("patched : %s" % target)
    print("md5 old : %s" % got)
    print("md5 new : %s" % new)

    if a.update_manifest:
        mf = os.path.join(REPO, "MANIFEST.md5")
        rel = os.path.relpath(os.path.abspath(target), REPO)
        if os.path.isfile(mf):
            lines = open(mf, encoding="utf-8").read().splitlines()
            out, hit = [], False
            for ln in lines:
                if ln.endswith("  " + rel):
                    out.append("%s  %s" % (new, rel)); hit = True
                else:
                    out.append(ln)
            if not hit:
                out.append("%s  %s" % (new, rel))
            out.sort()
            open(mf, "w", encoding="utf-8").write("\n".join(out) + "\n")
            print("MANIFEST.md5 updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
