# Gigabyte GA-H61M-DS2 — macOS High Sierra 10.13.6

> Gigabyte GA-H61M-DS2 — macOS High Sierra 10.13.6

ต้นทาง: [`GIGABIYE-GA-H61M-DS2-Hight-Sierra`](https://github.com/sealfx/GIGABIYE-GA-H61M-DS2-Hight-Sierra) (branch `master`)

## ข้อมูลเครื่อง / Hardware

| รายการ | ค่า |
|---|---|
| Mainboard / เมนบอร์ด | GIGABYTE GA-H61M-DS2 |
| CPU | Intel Core i3 @ 3.20GHz |
| RAM | 16GB (2 x 8GB) DDR3 |
| GPU | AMD Radeon RX570 8GB |
| Audio / เสียง | Realtek ALC887 |
| LAN / เน็ตเวิร์ก | Realtek 8111 |
| macOS | High Sierra 10.13.6 |

## ไฟล์ EFI

| ไฟล์ | md5 |
|---|---|
| [`EFI-GA-H61M-DS2-Hight-Sierra.zip`](./EFI-GA-H61M-DS2-Hight-Sierra.zip) | `ba8ee8af02f4ca4d277e7bc2f9c3909b` |

## ภาพหน้าจอ / Screenshots

- [`screenshots/Screen_Audio.png`](./screenshots/Screen_Audio.png)
- [`screenshots/Screen_GFX_Readion_RX570.png`](./screenshots/Screen_GFX_Readion_RX570.png)
- [`screenshots/Screen_Network.png`](./screenshots/Screen_Network.png)
- [`screenshots/Screen_Osx_Hightsierra10.13.6.png`](./screenshots/Screen_Osx_Hightsierra10.13.6.png)

## วิธีใช้ / Usage

1. ดาวน์โหลดไฟล์ EFI zip ในโฟลเดอร์นี้
2. แตก zip และคัดลอกโฟลเดอร์ `EFI/` ลง EFI System Partition (ESP) ของเครื่อง
3. ปรับ `config.plist` (SMBIOS / serial) ให้ตรงกับเครื่องของคุณก่อนใช้งาน
4. ตรวจสอบ md5 ของ zip ให้ตรงกับตารางด้านบนก่อนใช้

---

_ไฟล์นี้สร้างโดย `tools/build.py` — แก้ไขที่ generator ไม่ใช่แก้ไฟล์นี้ตรง ๆ_
