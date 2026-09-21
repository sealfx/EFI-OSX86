# Gigabyte GA-H61M-DS2 — macOS Catalina 10.15.4

> Gigabyte GA-H61M-DS2 — macOS Catalina 10.15.4

ต้นทาง: [`GIGABIYE-GA-H61M-DS2-Catalina`](https://github.com/sealfx/GIGABIYE-GA-H61M-DS2-Catalina) (branch `master`)

## ข้อมูลเครื่อง / Hardware

| รายการ | ค่า |
|---|---|
| Mainboard / เมนบอร์ด | GIGABYTE GA-H61M-DS2 |
| CPU | Intel Core i3 @ 3.20GHz |
| RAM | 16GB (2 x 8GB) DDR3 |
| GPU | AMD Radeon RX570 8GB |
| Audio / เสียง | Realtek ALC887 |
| LAN / เน็ตเวิร์ก | Realtek 8111 |
| macOS | Catalina 10.15.4 |

## ไฟล์ EFI

| ไฟล์ | md5 |
|---|---|
| [`EFI-GA-H61M-DS2-Catalina.zip`](./EFI-GA-H61M-DS2-Catalina.zip) | `7dd628bc6edd2749a92029500561eed9` |

## ภาพหน้าจอ / Screenshots

- [`screenshots/Screen_Audio_Device.png`](./screenshots/Screen_Audio_Device.png)
- [`screenshots/Screen_GFX_Readion_RX570.png`](./screenshots/Screen_GFX_Readion_RX570.png)
- [`screenshots/Screen_Network.png`](./screenshots/Screen_Network.png)
- [`screenshots/Screen_Osx_Catalina10.15.4.png`](./screenshots/Screen_Osx_Catalina10.15.4.png)

## วิธีใช้ / Usage

1. ดาวน์โหลดไฟล์ EFI zip ในโฟลเดอร์นี้
2. แตก zip และคัดลอกโฟลเดอร์ `EFI/` ลง EFI System Partition (ESP) ของเครื่อง
3. ปรับ `config.plist` (SMBIOS / serial) ให้ตรงกับเครื่องของคุณก่อนใช้งาน
4. ตรวจสอบ md5 ของ zip ให้ตรงกับตารางด้านบนก่อนใช้

---

_ไฟล์นี้สร้างโดย `tools/build.py` — แก้ไขที่ generator ไม่ใช่แก้ไฟล์นี้ตรง ๆ_
