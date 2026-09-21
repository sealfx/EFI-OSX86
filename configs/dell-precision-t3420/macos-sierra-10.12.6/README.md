# Dell Precision T3420 — macOS Sierra 10.12.x

> Dell Precision T3420 — macOS Sierra 10.12.x

ต้นทาง: [`DELL-Precision-T3420-Sierra`](https://github.com/sealfx/DELL-Precision-T3420-Sierra) (branch `master`)

## ข้อมูลเครื่อง / Hardware

| รายการ | ค่า |
|---|---|
| Workstation | Dell Precision T3420 |
| CPU | Intel Core i7-7700 (Quad Core, 8MB Cache, 3.6GHz, Turbo up to 4.20GHz) |
| Chipset | Intel C236 |
| RAM | 16GB (1 x 16GB) DDR4 2400MHz UDIMM Non-ECC |
| GPU | NVIDIA Quadro K1200 4GB (4 x mDP, Low Profile) |
| Optical drive | DVD-/+RW 8x |
| Storage | 256GB SSD |
| Audio / Sound | Integrated (Onboard) |
| Wireless / BT | None (ไม่มี) |
| macOS | Sierra 10.12.x |

## ไฟล์ EFI

| ไฟล์ | md5 |
|---|---|
| [`EFI_DELL_Precision_T3420_Sierra.zip`](./EFI_DELL_Precision_T3420_Sierra.zip) | `4990017221fc3b6a27bcb962d6b94669` |

## ภาพหน้าจอ / Screenshots

- [`screenshots/Screen_Audio_Device.png`](./screenshots/Screen_Audio_Device.png)
- [`screenshots/Screen_Dell_Precision_T3420.png`](./screenshots/Screen_Dell_Precision_T3420.png)
- [`screenshots/Screen_Ethernet_Device.png`](./screenshots/Screen_Ethernet_Device.png)
- [`screenshots/Screen_Nvidia_Quadro_K1200.png`](./screenshots/Screen_Nvidia_Quadro_K1200.png)
- [`screenshots/Screen_macOS_Sieera.png`](./screenshots/Screen_macOS_Sieera.png)

## เอกสารต้นฉบับ / Original notes

- [`notes/Dell_Workstation_T3420.txt`](./notes/Dell_Workstation_T3420.txt)

## ข้อสังเกต / Observations

- เวอร์ชัน macOS ไม่ตรงกันในเอกสารต้นฉบับ: README ของ repo เขียน **Sierra 10.12.3** แต่ description ของ repo และชื่อ screenshot ระบุ **10.12.6** — ยังไม่ได้ยืนยันว่าอันไหนถูก

## วิธีใช้ / Usage

1. ดาวน์โหลดไฟล์ EFI zip ในโฟลเดอร์นี้
2. แตก zip และคัดลอกโฟลเดอร์ `EFI/` ลง EFI System Partition (ESP) ของเครื่อง
3. ปรับ `config.plist` (SMBIOS / serial) ให้ตรงกับเครื่องของคุณก่อนใช้งาน
4. ตรวจสอบ md5 ของ zip ให้ตรงกับตารางด้านบนก่อนใช้

---

_ไฟล์นี้สร้างโดย `tools/build.py` — แก้ไขที่ generator ไม่ใช่แก้ไฟล์นี้ตรง ๆ_
