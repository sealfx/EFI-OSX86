# กติกาการแก้ไขไฟล์ / Contribution rules

## SOP หลัก (ผู้ใช้กำหนด — บังคับ)

1. **ศึกษา/สำรวจไฟล์ก่อนแก้ไขทุกครั้ง** — ห้ามแก้แบบเดาสุ่ม
2. **Pull ไฟล์ล่าสุดจากเซิร์ฟเวอร์ทุกครั้ง** ก่อนแก้ (เวอร์ชันบนเซิร์ฟเวอร์เปลี่ยนบ่อย)
3. **Recon** โครงสร้างและไฟล์ที่เกี่ยวข้องให้ครบถ้วนก่อนลงมือ
4. **เช็ค md5 ของไฟล์ก่อนแก้เสมอ**
5. **อ่านโค้ด ณ จุดที่จะแตะ** ก่อนแก้ไขทุกครั้ง
6. **Patch การแก้ไขผ่านสคริปต์ที่เตรียมไว้เท่านั้น** — ไม่แก้มือแบบสะเปะสะปะ

## วิธีปฏิบัติใน repo นี้

| ขั้น | คำสั่ง / วิธี |
|---|---|
| ดึงล่าสุด | `bash tools/sync.sh` (fetch/reset upstream แล้ว rebuild) |
| ตรวจ md5 ทั้งหมด | `bash tools/verify_md5.sh` |
| ดูไฟล์ต้นทาง | `_recon/upstream/<repo>/` (อ่านอย่างเดียว) |
| แก้ไฟล์ | `python3 tools/apply_patch.py --file <f> --expect-md5 <md5> --patch <d.diff> [--dry-run]` |
| สร้างใหม่หลังแก้ generator | `python3 tools/build.py` |

### ห้าม
- แก้ไฟล์ที่ generate แล้ว (`configs/**`, `shared/**`, `README.md`, `docs/HARDWARE-MATRIX.md`, `MANIFEST.md5`) ด้วยมือ
  → แก้ที่ `tools/build.py` แล้วรันใหม่
- แตก/บีบอัด zip ใหม่ (ต้องรักษาไบต์เดิม md5 ต้องตรง baseline)
- ลบ/ย้ายไฟล์ใน `upstream/` (เป็นสำเนาเพื่อ traceability)
- commit โดยไม่รัน `verify_md5.sh` ผ่าน

### การเพิ่มเครื่องใหม่
1. ใส่ entry ใหม่ใน `ENTRIES` ของ `tools/build.py` (พร้อม md5 ของ EFI zip ทุกไฟล์)
2. เพิ่มชื่อ repo ต้นทางในรายการของ `sync.sh` (ดึงจาก `build.py --list-repos` อัตโนมัติ)
3. `bash tools/sync.sh` แล้วตรวจว่า `verify_md5.sh` ผ่าน
