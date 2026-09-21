# <ชื่อเครื่อง / Machine name>

> <Machine name in English>

ต้นทาง: [`<source-repo>`](https://github.com/sealfx/<source-repo>) (branch `main`)

## ข้อมูลเครื่อง / Hardware

| รายการ | ค่า |
|---|---|
| Mainboard / เครื่อง | |
| CPU | |
| Chipset | |
| RAM | |
| GPU | |
| Audio / เสียง | |
| LAN / เน็ตเวิร์ก | |
| Storage | |
| Display | |
| macOS | |

## ไฟล์ EFI

| ไฟล์ | md5 |
|---|---|
| `EFI-XXX.zip` | `` |

## ภาพหน้าจอ / Screenshots

- `screenshots/xxx.png`

## ข้อสังเกต / Observations

- _(ระบุเฉพาะสิ่งที่พบจริง / only verified facts)_

## วิธีใช้ / Usage

1. ดาวน์โหลดไฟล์ EFI zip ในโฟลเดอร์นี้
2. แตก zip และคัดลอกโฟลเดอร์ `EFI/` ลง EFI System Partition (ESP)
3. ปรับ `config.plist` (SMBIOS / serial) ให้ตรงกับเครื่องของคุณก่อนใช้งาน
4. ตรวจสอบ md5 ของ zip ให้ตรงกับตารางด้านบนก่อนใช้

---
_โฟลเดอร์ตัวอย่าง / Folder layout_

```
configs/<machine-slug>/<macos-slug>/
├── README.md
├── EFI-<machine>.zip
├── screenshots/*.png
└── notes/*.txt        (ถ้ามี)
```
