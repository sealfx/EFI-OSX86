# แก้ปัญหา / Troubleshooting

รวมอาการ–ต้นเหตุ–วิธีแก้ **ที่บันทึกไว้จริง** จากแต่ละชุดใน repo นี้
เอกสารนี้แยกชัดระหว่าง "มีหลักฐาน" และ "ยังไม่มีข้อมูล" เพื่อไม่ให้เข้าใจผิด

---

## ระดับหลักฐานของแต่ละชุด

| ชุด | สถานะเอกสาร |
|---|---|
| Dell Precision T3420 — Sequoia 15.7.9 | ✅ มีบันทึกครบ (อาการ, root cause, สิ่งที่ทดสอบแล้วไม่ใช่สาเหตุ) |
| HP Pavilion 24-b212d — High Sierra | 🟡 มีบันทึกสั้น ๆ จาก README ต้นฉบับ |
| GA-H61M-DS2 (Catalina / High Sierra) | ⚪️ ไม่มีบันทึกปัญหา (มีแต่สเปกเครื่อง) |
| Dell T3420 (High Sierra / Sierra) | ⚪️ ไม่มีบันทึกปัญหา |
| Dell T7450 AIO — High Sierra | ⚪️ ไม่มีบันทึกปัญหา |
| Mac Pro Late 2013 — Sequoia | ⚪️ ไม่มีเอกสารประกอบในชุดที่อัปโหลด |

---

## 1) Dell Precision T3420 — macOS Sequoia 15.7.9 ✅

**(ก) สีเพี้ยน ฟ้า↔ส้ม / จอเขียว / `Framebuffer Depth = 30-bit`**

| | |
|---|---|
| ต้นเหตุ | SMBIOS (board-id) `iMac18,3` ทำให้ macOS จัดพอร์ตจอ/สีผิด |
| วิธีแก้ | เปลี่ยน SMBIOS เป็น **`MacPro7,1`** → สีถูกต้อง |

**(ข) จอค้าง/ดับหลังเข้าหน้าจอ (เหลือแต่ Cursor)**

| | |
|---|---|
| ต้นเหตุ | สถานะจอถูกตัดเป็น offline |
| วิธีแก้ | boot-arg **`igfxonln=1`** (force display online) |

**ทดสอบแล้ว "ไม่ใช่สาเหตุ" — ไม่ต้องลองซ้ำ**
- เวอร์ชัน OpenCore / Lilu / WhateverGreen (ทดสอบ 3 ชุด: 1.7.0/1.7.2 → 1.6.9 → 1.6.8 + OC 1.0.6/1.0.7)
- EDID override ที่ `/Library/Displays/...`
- `framebuffer-con0-type = DVI` (จอไม่ขึ้น) / `DP` (จอดำ)
- `disable-agdc`, `AAPL,GfxYTile`, `agdpmod=ignore`, `igfxfcms=1`
- ลบ `framebuffer-fbmem` / `stolenmem` → ค้าง
- OCLP 2.5.1 → "No Root Patches required"
- SMBIOS `iMac18,1` → จอดำ

**บทเรียนการทำงานของเครื่องนี้**
- มี **2 EFI** สลับกันได้ → ฝัง marker ใน boot-args: `espm=efi` (EFI หลัก disk0s1) / `espm=boot` (EFI สำรอง disk0s2)
  ตรวจก่อนสรุปผลทุกครั้ง: `nvram boot-args | grep -o 'espm=[a-z]*'`
- ค่าที่เชื่อถือได้: `system_profiler SPDisplaysDataType` · `kmutil showloaded | grep -iE 'lilu|whatevergreen|KBL'` · `nvram boot-args`
- ESP ถูก unmount หลังรีบูตทุกครั้ง → `sudo diskutil mount disk0s1` ก่อนแก้ไฟล์

## 2) HP Pavilion 24-b212d AIO — High Sierra 🟡

- **Intel HD Graphics 630** → ใช้งานได้
- **NVIDIA GeForce 930MX 4GB** → ยังไม่สำเร็จ (ตามที่เจ้าของบันทึกไว้ใน README ต้นฉบับ)

## 3) อาการทั่วไปที่พบได้บ่อย

| อาการ | จุดที่ควรตรวจ |
|---|---|
| บูตค้างหน้าจอ Apple | เพิ่ม boot-arg `-v` ดูข้อความ แล้วถ่ายรูปไว้ |
| kext ไม่โหลด | ตรวจ `Kernel > Add` ว่าเปิด `Enabled=true` และลำดับถูก (Lilu ต้องมาก่อน kext ที่พึ่ง Lilu) |
| เน็ต/เสียงไม่ทำงาน | ตรวจ device properties + boot-arg เฉพาะชุด (`alcid=`, `igfxonln=`) |
| จอดำแต่เครื่องทำงาน | ตรวจ `AAPL,ig-platform-id` / connector type ให้ตรงกับพอร์ตที่ใช้จริง |
| ใช้ OpenCore ผิดรุ่น | `OpenCore.efi` + `BOOTx64.efi` + drivers ต้องเป็นเวอร์ชันชุดเดียวกัน |

## 4) แหล่งอ้างอิงมาตรฐาน

- Dortania OpenCore Install Guide — https://dortania.github.io/OpenCore-Install-Guide/
- OpenCore Configuration manual (ใน OpenCorePkg/Docs) — https://github.com/acidanthera/OpenCorePkg
- รายการ kext + เวอร์ชันที่ตรวจพบใน repo นี้ — [`CREDITS.md`](./CREDITS.md)

> ถ้าคุณแก้ปัญหาชุดไหนได้ กรุณาเปิด Issue แจ้ง เพื่อให้เพิ่มลงเอกสารนี้ (ดู `.github/ISSUE_TEMPLATE`)
