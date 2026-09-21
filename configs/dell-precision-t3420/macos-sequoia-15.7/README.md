# Dell Precision T3420 (i7-7700 / Intel HD 630) — macOS Sequoia 15.7.9

> Dell Precision T3420 (i7-7700 + Intel HD 630 iGPU) — macOS Sequoia 15.7.9

ที่มา: ไฟล์ที่อัปโหลดโดยเจ้าของ repo (local upload) — ข้อมูลสกัดจาก `OC/config.plist` และรายการไฟล์ใน zip จริง

## ข้อมูลเครื่อง / Hardware

| รายการ | ค่า |
|---|---|
| Machine | Dell Precision T3420 (i7-7700 + iGPU) |
| CPU | Intel Core i7-7700 |
| GPU | Intel HD Graphics 630 (iGPU) — เร่งความเร็วได้ 1536 MB, Metal 3 |
| SMBIOS | **MacPro7,1** — ตัวชี้ขาดที่ทำให้สีถูกต้อง (iMac18,3 ทำให้สีเพี้ยน ฟ้า↔ส้ม) |
| boot-args | `keepsyms=1 debug=0x100 alcid=11 -no_compat_check -wegnoegpu igfxonln=1 espm=boot` |
| OpenCore | 1.0.8 |
| Kext | 17 รายการ: Lilu, VirtualSMC(+SMCProcessor/SuperIO/Battery/Light/DellSensors), WhateverGreen, AppleALC/AppleALCU (alcid=11), IntelMausi + IntelMausiEthernet, USBToolBox/UTBDefault, XHCI-unsupported, AMFIPass, RestrictEvents |
| iGPU properties | `AAPL,ig-platform-id=00001659` · `device-id=16590000` · `framebuffer-patch-enable` · `framebuffer-con1/-con2-type=HDMI` · `enable-hdmi-dividers-fix` · `framebuffer-stolenmem=00003001` (≈19 MB) |
| ธีม / Theme | GoldenGate (`PickerMode=External`, `PickerVariant=Acidanthera\GoldenGate`) |
| macOS | Sequoia 15.7.9 (24G830) |

## ไฟล์ EFI

| ไฟล์ | md5 |
|---|---|
| [`EFI-Dell-Precision-3420.zip`](./EFI-Dell-Precision-3420.zip) | `29068d3fb8d250364cf6fecf5d2761f7` |

## เอกสารต้นฉบับ / Original notes

- [`notes/EFI-Dell-Precision-3420.md`](./notes/EFI-Dell-Precision-3420.md)

## ข้อสังเกต / Observations

- **จุดสำคัญที่แก้สำเร็จ:** สีเพี้ยน (Framebuffer Depth 30-bit) แก้ด้วยการเปลี่ยน SMBIOS จาก `iMac18,3` เป็น **`MacPro7,1`** และอาการจอค้าง/ดับหลังเข้าหน้าจอ แก้ด้วย boot-arg **`igfxonln=1`** — ตัวอื่น (เวอร์ชัน OpenCore/Lilu/WhateverGreen, EDID override, `agdpmod=ignore`, OCLP) ทดสอบแล้ว **ไม่ใช่สาเหตุ**
- เอกสารต้นฉบับเรียกเครื่องว่า **Dell OptiPlex** (i7-7700 / Intel HD 630) แต่ชื่อไฟล์ EFI และโฟลเดอร์ใน zip เป็น **Dell Precision T3420** — ยังไม่ยืนยันว่าเป็นเครื่องเดียวกัน หรือเขียนชื่อรุ่นผิด จึงเก็บชื่อตามไฟล์ EFI และคงข้อความเดิมไว้ในเอกสาร
- ค่าที่สกัดจาก `OC/config.plist` ตรงกับเอกสารทุกจุด (SMBIOS, boot-args, ig-platform-id, stolenmem)
- ใน zip มีไฟล์สำรอง `config.plist.bak1..bak22`, `config.plist.presafe-*` และ `_old-kexts/` ติดมาด้วย — เก็บไว้ตามต้นฉบับ ไม่ได้ตัดออก
- เครื่องนี้มี 2 EFI ที่สลับเองได้ → ฝัง marker ใน boot-args (`espm=efi` = EFI หลัก, `espm=boot` = EFI สำรอง) ชุดนี้เป็น `espm=boot`
- 🔒 **ไฟล์นี้ถูก sanitize ก่อนเผยแพร่** — ล้าง `SystemSerialNumber`, `MLB`, `SystemUUID`, `ROM` ในไฟล์ `config.plist*` ทุกไฟล์ภายใน zip (30 ไฟล์) แล้ว โดย**คง `SystemProductName = MacPro7,1` ไว้** เพราะเป็นค่าที่จำเป็นต่อการใช้งาน · md5 ปัจจุบัน `29068d3fb8d250364cf6fecf5d2761f7` (ต่างจากไฟล์ต้นฉบับที่อัปโหลด `564dc53c43a240fef881c2d548f18f08`) → **ต้องสร้าง SMBIOS ของตัวเองก่อนใช้**

## วิธีใช้ / Usage

1. ดาวน์โหลดไฟล์ EFI zip ในโฟลเดอร์นี้
2. แตก zip และคัดลอกโฟลเดอร์ `EFI/` ลง EFI System Partition (ESP) ของเครื่อง
3. ปรับ `config.plist` (SMBIOS / serial) ให้ตรงกับเครื่องของคุณก่อนใช้งาน
4. ตรวจสอบ md5 ของ zip ให้ตรงกับตารางด้านบนก่อนใช้

---

_ไฟล์นี้สร้างโดย `tools/build.py` — แก้ไขที่ generator ไม่ใช่แก้ไฟล์นี้ตรง ๆ_
