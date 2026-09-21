# tools/

| ไฟล์ | หน้าที่ |
|---|---|
| `build.py` | generator: สร้าง tree (`configs/`, `shared/`, `upstream/`), README ทุกชุด, `docs/HARDWARE-MATRIX.md`, `repo-meta.json`, `MANIFEST.md5` และตรวจ md5 ของ EFI zip กับ baseline |
| `sync.sh` | idempotent: fetch/reset ต้นทางจาก GitHub (sealfx) แล้วเรียก `build.py` + `verify_md5.sh` |
| `verify_md5.sh` | ตรวจ md5 ทุกไฟล์เทียบ `MANIFEST.md5` — exit 0 = ผ่าน, exit 1 = ไม่ตรง |
| `apply_patch.py` | patch ไฟล์แบบบังคับ md5 pre-check (ตาม SOP) มี `--dry-run` และ `--update-manifest` |

```bash
python3 tools/build.py --list-repos        # repo ต้นทาง + branch
python3 tools/apply_patch.py --help
```
