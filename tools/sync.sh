#!/usr/bin/env bash
# สร้าง/อัปเดต EFI-OSX86 จาก source ที่มีอยู่ในเครื่อง (ไม่ต่อเน็ต)
#
# ต้องมี source 2 ที่ (ไม่ได้ commit ขึ้น repo เพราะมีไฟล์ EFI ขนาดใหญ่):
#   ../_recon/upstream/<repo>/   สำเนา repo ต้นทางเดิม (6 ชุด)
#   ../_recon/local/<name>/      ไฟล์ที่เจ้าของ repo อัปโหลดเอง (Dell Sequoia, Mac Pro Late 2013)
#
# ไฟล์ EFI ที่ใช้งานจริงอยู่ใน configs/** ของ repo นี้แล้ว — sync.sh มีไว้สำหรับ "สร้างใหม่"
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(dirname "$HERE")"
ROOT="$(dirname "$REPO")"

missing=0
for d in "$ROOT/_recon/upstream" "$ROOT/_recon/local"; do
  if [ ! -d "$d" ]; then echo "!! ไม่พบ source: $d" >&2; missing=1; fi
done
if [ "$missing" != "0" ]; then
  echo "   ต้องมี source ในเครื่องก่อนจึงจะ rebuild ได้ (ดู docs/CONTRIBUTING.md)" >&2
  exit 2
fi

echo "== build"
python3 "$HERE/build.py"
echo "== verify"
bash "$HERE/verify_md5.sh"
