# tools/

| ไฟล์ | หน้าที่ |
|---|---|
| `build.py` | generator (สำหรับผู้ดูแล): สร้าง `configs/**`, `shared/**`, `upstream/**`, README ทุกชุด, `docs/HARDWARE-MATRIX.md`, `repo-meta.json`, `MANIFEST.md5` และตรวจ md5 กับ baseline |
| `verify_md5.sh` | ตรวจ md5 ทุกไฟล์เทียบ `MANIFEST.md5` — ใช้ได้ทั้ง macOS และ Linux (รันใน CI ด้วย) |
| `sync.sh` | rebuild จาก source ในเครื่อง (`_recon/upstream`, `_recon/local`) — **ไม่ต่อเน็ต** |
| `apply_patch.py` | patch ไฟล์แบบบังคับ md5 pre-check (ตาม SOP) มี `--dry-run`, `--update-manifest` |

```bash
bash tools/verify_md5.sh                    # ตรวจความถูกต้อง (ใช้ได้ทุกคน)
python3 tools/apply_patch.py --help         # เครื่องมือแก้ไฟล์แบบมี md5 gate
python3 tools/build.py --list-repos         # ดูรายการ source
```

> **สำหรับผู้ใช้ทั่วไป:** ไฟล์ EFI ที่ใช้งานจริงอยู่ใน `configs/**` แล้ว ไม่ต้องรัน `build.py`
> `build.py` / `sync.sh` มีไว้สำหรับผู้ดูแล repo ที่มี source ต้นทางใน `_recon/` เท่านั้น
