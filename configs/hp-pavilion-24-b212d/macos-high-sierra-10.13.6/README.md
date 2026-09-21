# HP Pavilion 24-b212d (Z8G27AA#AKL) AIO — macOS High Sierra 10.13.6

> HP Pavilion 24-b212d (Z8G27AA#AKL) AIO — macOS High Sierra 10.13.6

ต้นทาง: [`HP-Pavilion-24-b212d-Z8G27AA-AKL-AIO`](https://github.com/sealfx/HP-Pavilion-24-b212d-Z8G27AA-AKL-AIO) (branch `master`)

## ข้อมูลเครื่อง / Hardware

| รายการ | ค่า |
|---|---|
| Machine | HP Pavilion 24-b212d Z8G27AA#AKL (23.8" All-in-One) |
| CPU | Intel Core i5-7400T 2.4GHz |
| RAM | 16GB DDR4 2133MHz |
| GPU | Intel HD Graphics 630 — ใช้งานได้ |
| GPU (ตัวที่สอง) | NVIDIA GeForce 930MX 4GB — ยังไม่สำเร็จ (Not success) |
| Display | 23.8" FHD IPS Touch |
| macOS | High Sierra 10.13.6 |

## ไฟล์ EFI

| ไฟล์ | md5 |
|---|---|
| [`EFI_HP_Pavilion_24-b212d_Z8G27AA_AKL_AIO.zip`](./EFI_HP_Pavilion_24-b212d_Z8G27AA_AKL_AIO.zip) | `86494c5d8bd03634c5587b45ed3ece5f` |
| [`EFI_OC_Any.zip`](./EFI_OC_Any.zip) | `488b78b476ff7b034cf366713e822302` |

## ภาพหน้าจอ / Screenshots

<details><summary>คลิกเพื่อดูภาพทั้งหมด (5 ภาพ)</summary>

**Screen_Audio.png**

![`Screen_Audio.png`](./screenshots/Screen_Audio.png)

**Screen_Ethernet.png**

![`Screen_Ethernet.png`](./screenshots/Screen_Ethernet.png)

**Screen_Hardware.png**

![`Screen_Hardware.png`](./screenshots/Screen_Hardware.png)

**Screen_Hight_Siera_10.13.6.png**

![`Screen_Hight_Siera_10.13.6.png`](./screenshots/Screen_Hight_Siera_10.13.6.png)

**Screen_Intel_Gfx_HD_630.png**

![`Screen_Intel_Gfx_HD_630.png`](./screenshots/Screen_Intel_Gfx_HD_630.png)

</details>

## ข้อสังเกต / Observations

- repo ต้นฉบับบรรจุ EFI สองชุด: ชุดเฉพาะเครื่องนี้ และ `EFI_OC_Any.zip` (คัดลอกไปไว้ที่ `shared/opencore-any/` แล้ว)

## วิธีใช้ / Usage

1. ดาวน์โหลดไฟล์ EFI zip ในโฟลเดอร์นี้
2. แตก zip และคัดลอกโฟลเดอร์ `EFI/` ลง EFI System Partition (ESP) ของเครื่อง
3. ปรับ `config.plist` (SMBIOS / serial) ให้ตรงกับเครื่องของคุณก่อนใช้งาน
4. ตรวจสอบ md5 ของ zip ให้ตรงกับตารางด้านบนก่อนใช้

---

_ไฟล์นี้สร้างโดย `tools/build.py` — แก้ไขที่ generator ไม่ใช่แก้ไฟล์นี้ตรง ๆ_
