# Dell Precision T3420 — macOS High Sierra 10.13.6

> Dell Precision T3420 — macOS High Sierra 10.13.6

ต้นทาง: [`DELL-Precision-T3420-Hight-Sierra`](https://github.com/sealfx/DELL-Precision-T3420-Hight-Sierra) (branch `master`)

## ข้อมูลเครื่อง / Hardware

| รายการ | ค่า |
|---|---|
| Workstation | Dell Precision T3420 |
| CPU | Intel Core i7-7700 (4C/8T, 3.6GHz, Turbo 4.20GHz, 8MB) |
| Chipset | Intel C236 |
| RAM | 16GB (1 x 16GB) DDR4 2400MHz UDIMM Non-ECC |
| GPU | NVIDIA Quadro K1200 4GB (4 x mDP, Low Profile) |
| Storage | 256GB SSD |
| macOS | High Sierra 10.13.6 |

## ไฟล์ EFI

| ไฟล์ | md5 |
|---|---|
| [`EFI_DELL_Precision_T3420_Hight_Sierra.zip`](./EFI_DELL_Precision_T3420_Hight_Sierra.zip) | `b0bedbcdf7e93a5780477dc8a168aeef` |

## ภาพหน้าจอ / Screenshots

- [`screenshots/Screen_Audio_AlC255.png`](./screenshots/Screen_Audio_AlC255.png)
- [`screenshots/Screen_Dell_Precision_T3420.png`](./screenshots/Screen_Dell_Precision_T3420.png)
- [`screenshots/Screen_Ethernet.png`](./screenshots/Screen_Ethernet.png)
- [`screenshots/Screen_Hight_Sierra_10.13.6.png`](./screenshots/Screen_Hight_Sierra_10.13.6.png)
- [`screenshots/Screen_Nvidia_Quadro_K1200.png`](./screenshots/Screen_Nvidia_Quadro_K1200.png)

## วิธีใช้ / Usage

1. ดาวน์โหลดไฟล์ EFI zip ในโฟลเดอร์นี้
2. แตก zip และคัดลอกโฟลเดอร์ `EFI/` ลง EFI System Partition (ESP) ของเครื่อง
3. ปรับ `config.plist` (SMBIOS / serial) ให้ตรงกับเครื่องของคุณก่อนใช้งาน
4. ตรวจสอบ md5 ของ zip ให้ตรงกับตารางด้านบนก่อนใช้

---

_ไฟล์นี้สร้างโดย `tools/build.py` — แก้ไขที่ generator ไม่ใช่แก้ไฟล์นี้ตรง ๆ_
