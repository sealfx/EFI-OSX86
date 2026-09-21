# Dell Precision T7450 AIO — macOS High Sierra 10.13.6

> Dell Precision T7450 AIO — macOS High Sierra 10.13.6

ต้นทาง: [`DELL-Precision-T7450-AIO`](https://github.com/sealfx/DELL-Precision-T7450-AIO) (branch `master`)

## ข้อมูลเครื่อง / Hardware

| รายการ | ค่า |
|---|---|
| Machine | Dell Precision T7450 AIO (23.8" All-in-One) |
| CPU | Intel Core i5-7500 |
| RAM | 16GB DDR4 |
| Storage | 256GB SSD (+ NVMe M.2 Samsung ตาม screenshot) |
| Display | 23.8" FHD Touch |
| GPU | Intel HD Graphics 630 (ใช้ได้) |
| macOS | High Sierra 10.13.6 |

## ไฟล์ EFI

| ไฟล์ | md5 |
|---|---|
| [`EFI_DELL_Precision_T7450_AIO.zip`](./EFI_DELL_Precision_T7450_AIO.zip) | `e61585b43b9fe13365205e386cb756b0` |

## ภาพหน้าจอ / Screenshots

<details><summary>คลิกเพื่อดูภาพทั้งหมด (5 ภาพ)</summary>

**Screen_Audio.png**

![`Screen_Audio.png`](./screenshots/Screen_Audio.png)

**Screen_Dell_Precision_7450_Spec.png**

![`Screen_Dell_Precision_7450_Spec.png`](./screenshots/Screen_Dell_Precision_7450_Spec.png)

**Screen_GFX_HD_630.png**

![`Screen_GFX_HD_630.png`](./screenshots/Screen_GFX_HD_630.png)

**Screen_MacOs_Hight_Sierra_10.13.6.png**

![`Screen_MacOs_Hight_Sierra_10.13.6.png`](./screenshots/Screen_MacOs_Hight_Sierra_10.13.6.png)

**Screen_Nvme_M2_Sansung.png**

![`Screen_Nvme_M2_Sansung.png`](./screenshots/Screen_Nvme_M2_Sansung.png)

</details>

## ข้อสังเกต / Observations

- Readme ต้นฉบับเขียนชื่อรุ่นว่า "DELL OptiPlex T7450 AIO" แต่ชื่อ repo และชื่อไฟล์ EFI เป็น "DELL_Precision_T7450_AIO" — เก็บชื่อเดิมไว้ทั้งคู่ ไม่ได้แก้ให้ตรงกัน

## วิธีใช้ / Usage

1. ดาวน์โหลดไฟล์ EFI zip ในโฟลเดอร์นี้
2. แตก zip และคัดลอกโฟลเดอร์ `EFI/` ลง EFI System Partition (ESP) ของเครื่อง
3. ปรับ `config.plist` (SMBIOS / serial) ให้ตรงกับเครื่องของคุณก่อนใช้งาน
4. ตรวจสอบ md5 ของ zip ให้ตรงกับตารางด้านบนก่อนใช้

---

_ไฟล์นี้สร้างโดย `tools/build.py` — แก้ไขที่ generator ไม่ใช่แก้ไฟล์นี้ตรง ๆ_
