# Dell Precision T3420 (i7-7700 / Intel HD 630) — macOS Sequoia 15.7.9

> Dell Precision T3420 (i7-7700 + Intel HD 630 iGPU) — macOS Sequoia 15.7.9

ที่มา: ไฟล์ที่อัปโหลดโดยเจ้าของ repo (local upload) — ข้อมูลสกัดจาก `OC/config.plist` และรายการไฟล์ใน zip จริง

## ข้อมูลเครื่อง / Hardware

| รายการ | ค่า |
|---|---|
| Machine | Dell Precision T3420 (i7-7700 + iGPU) |
| CPU | Intel Core i7-7700 |
| GPU | Intel HD Graphics 630 (iGPU) — เร่งความเร็วได้ 1536 MB · Metal 3 |
| SMBIOS | **MacPro7,1** — ตัวชี้ขาดที่ทำให้สีถูกต้อง (iMac18,3 ทำให้สีเพี้ยน ฟ้า↔ส้ม) |
| boot-args | `keepsyms=1 debug=0x100 alcid=11 -no_compat_check -wegnoegpu igfxonln=1 espm=boot` |
| OpenCore | 1.0.8 |
| Kext | 17 รายการ: Lilu, VirtualSMC(+SMCProcessor/SuperIO/Battery/Light/DellSensors), WhateverGreen, AppleALC/AppleALCU (alcid=11), IntelMausi + IntelMausiEthernet, USBToolBox/UTBDefault, XHCI-unsupported, AMFIPass, RestrictEvents |
| iGPU properties | `AAPL,ig-platform-id=00001659` · `device-id=16590000` · `framebuffer-patch-enable` · `framebuffer-con1-type=HDMI` · `framebuffer-con2-type=DP` · `enable-hdmi-dividers-fix` · `framebuffer-stolenmem=00003001` (≈19 MB) |
| จอ / Display | DELL E2216H 1920×1080 @60Hz — ต่อผ่าน **DP** (พอร์ต DP ทุกช่องใช้ได้) |
| จอพร้อมกัน | **1 จอ** — เอกสารใน zip ระบุว่า 2 จอพร้อมกัน (HDMI + DP) **ทำไม่ได้** บนเครื่องนี้ |
| USB | USB 2.0 (XHCI) 15 พอร์ต · **USB 3.0 SuperSpeed ไม่ถูกสร้าง** → อุปกรณ์ USB3 ต้องต่อพอร์ต USB2 |
| ธีม / Theme | GoldenGate (`PickerMode=External`, `PickerVariant=Acidanthera\GoldenGate`) |
| macOS | Sequoia 15.7.9 (24G830) |

## ไฟล์ EFI

| ไฟล์ | md5 |
|---|---|
| [`EFI-Dell-Precision-3420.zip`](./EFI-Dell-Precision-3420.zip) | `d712d5aee660aed97d952033398ae9d7` |

## เอกสารต้นฉบับ / Original notes

- [`notes/EFI-Dell-Precision-3420.md`](./notes/EFI-Dell-Precision-3420.md)

## ข้อสังเกต / Observations

- **จุดสำคัญที่แก้สำเร็จ:** สีเพี้ยน (Framebuffer Depth 30-bit) แก้ด้วยการเปลี่ยน SMBIOS จาก `iMac18,3` เป็น **`MacPro7,1`** และอาการจอค้าง/ดับหลังเข้าหน้าจอ แก้ด้วย boot-arg **`igfxonln=1`**
- ⚠️ **ยังไม่ยืนยันเรื่อง 2 จอ** — เอกสารใน zip (อัปเดต 2026-09-22 04:40) ระบุว่า **2 จอพร้อมกัน (HDMI + DP) ทำไม่ได้บนเครื่องนี้**: พอร์ต HDMI ขับด้วย macOS ไม่ได้ (ลองประกาศ type HDMI ที่ port 5 และ port 7 แล้วไม่ขึ้นทั้งคู่ — น่าจะเป็นข้อจำกัด BIOS/VBT) และได้ **1 จอผ่าน DP เสมอ** · ตัวเลือกที่ยังไม่ได้ลอง: SMBIOS `Macmini8,1` · (ผู้ใช้อัปโหลดไฟล์นี้พร้อมข้อความว่าใช้ได้ 2 จอแล้ว — **ขัดกับเอกสารที่แนบมา** จึงยังไม่ยืนยัน)
- เวอร์ชันนี้เปลี่ยน `framebuffer-con2-type` จาก `00080000` (HDMI) → **`00040000` (DP)** เพื่อให้พอร์ต DP ของเครื่องใช้งานได้
- **อย่าใช้ `-alldata` + ประกาศ 3 คอนเนกเตอร์** — ทำให้จอดับ ให้ใช้แบบ `-type` ธรรมดา (con1=HDMI, con2=DP) ซึ่งเสถียร
- ปัญหา USB 3.0: macOS สร้างพอร์ต USB2 15 พอร์ต แต่ SuperSpeed = 0 เพราะ `UTBDefault.kext` เป็น placeholder ที่ไม่มีข้อมูลพอร์ต → ต้องสร้าง USB port map จริงด้วย USBToolBox
- เอกสารตั้งชื่อเครื่องเพียง **Dell (i7-7700 / Intel HD 630)** ไม่ได้ระบุรุ่น — ชื่อไฟล์ EFI และโฟลเดอร์ใน zip เป็น `EFI-Dell-Precision-3420` จึงคงชื่อตามไฟล์ EFI
- 🔒 **ไฟล์นี้ถูก sanitize ก่อนเผยแพร่** — ล้าง `SystemSerialNumber`, `MLB`, `SystemUUID`, `ROM` ใน `config.plist*` ทุกไฟล์ใน zip (30 ไฟล์) โดยคง `SystemProductName = MacPro7,1` ไว้ · md5 ปัจจุบัน `d712d5aee660aed97d952033398ae9d7` → **ต้องสร้าง SMBIOS ของตัวเองก่อนใช้**
- ใน zip มีไฟล์สำรอง `config.plist.bak*` (ถึง bak33) และ `_kexts/_old-kexts/` ติดมาด้วย — เก็บตามต้นฉบับ
- เครื่องนี้มี 2 EFI ที่สลับเองได้ → ฝัง marker ใน boot-args (`espm=efi` = EFI หลัก, `espm=boot` = EFI สำรอง) ชุดนี้เป็น `espm=boot`

## วิธีใช้ / Usage

1. ดาวน์โหลดไฟล์ EFI zip ในโฟลเดอร์นี้
2. แตก zip และคัดลอกโฟลเดอร์ `EFI/` ลง EFI System Partition (ESP) ของเครื่อง
3. ปรับ `config.plist` (SMBIOS / serial) ให้ตรงกับเครื่องของคุณก่อนใช้งาน
4. ตรวจสอบ md5 ของ zip ให้ตรงกับตารางด้านบนก่อนใช้

---

_ไฟล์นี้สร้างโดย `tools/build.py` — แก้ไขที่ generator ไม่ใช่แก้ไฟล์นี้ตรง ๆ_
