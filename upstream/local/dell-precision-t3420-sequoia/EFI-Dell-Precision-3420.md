# สรุปงาน (ฉบับสมบูรณ์): Dell OptiPlex + Intel HD 630 + macOS Sequoia — **แก้สำเร็จ** ✅

_อัปเดตล่าสุด: 2026-09-22 02:00 (+07)_

## 1) ผลลัพธ์
เครื่อง **Dell OptiPlex (i7-7700 / Intel HD 630)** บน **macOS Sequoia 15.7.9 (24G830)**
→ **เปิด accel ได้ (1536 MB, Metal 3) และสีถูกต้อง** ทั้งคู่พร้อมกัน

## 2) กุญแจสำคัญ (root cause ที่เจอ)
| อาการ | สาเหตุที่แท้จริง | วิธีแก้ |
|---|---|---|
| สีเพี้ยน ฟ้า↔ส้ม / จอเขียว / `Framebuffer Depth = 30-bit` | **SMBIOS (board-id) `iMac18,3`** ทำให้ macOS จัดท่อจอ/สีผิด | เปลี่ยนเป็น **`MacPro7,1`** → **สีถูก** |
| จอค้าง/ดับหลังเข้าหน้าจอ (เหลือแต่ Cursor) | สถานะจอถูกตัดเป็น offline | boot-arg **`igfxonln=1`** (force display online) |

## 3) ค่าที่ใช้งานจริงตอนนี้ (ทั้ง EFI หลักและ EFI สำรอง)
| รายการ | ค่า |
|---|---|
| SMBIOS | **MacPro7,1** |
| boot-args | `keepsyms=1 debug=0x100 alcid=11 -no_compat_check -wegnoegpu igfxonln=1` (+ marker `espm=efi` / `espm=boot`) |
| iGPU DeviceProperties | `AAPL,ig-platform-id = 00001659` (HD 620) · `device-id = 16590000` · `enable-hdmi-dividers-fix` · `framebuffer-con1/-con2-type = HDMI` · `framebuffer-patch-enable` · `framebuffer-stolenmem = 19 MB` |
| OpenCore | **1.0.8** (+ `BOOTx64.efi`, `OpenRuntime.efi`, `OpenCanopy.efi`, `ResetNvramEntry.efi`) |
| Lilu / WhateverGreen | **1.7.2 / 1.7.0** = เวอร์ชันล่าสุดบน GitHub |
| kext อื่น | AMFIPass, VirtualSMC(+SMC*), AppleALC(alcid=11), IntelMausi(Ethernet), RestrictEvents, USBToolBox/UTBDefault, XHCI-unsupported |
| ธีม OpenCore | **GoldenGate** (`Misc/Boot/PickerMode = External`, `PickerVariant = Acidanthera\GoldenGate`) — **ไม่แตะ `OpenCore.efi`** |
| จอ | DELL E2216H 1920×1080 @60Hz (ผ่าน HDMI→VGA) |

## 4) ที่ทดลองแล้ว "ไม่ใช่สาเหตุ" (บันทึกไว้ ไม่ต้องลองซ้ำ)
- เวอร์ชัน OpenCore/Lilu/WhateverGreen (ทดสอบ 3 ชุด: 1.7.0/1.7.2 → 1.6.9 → 1.6.8 + OC 1.0.6/1.0.7) — depth ยัง 30-bit เท่าเดิม
- EDID override ที่ `/Library/Displays/...` (macOS ไม่อ่าน — พิสูจน์ด้วย EDID ที่ระบบใช้จริง)
- `framebuffer-con0-type = DVI` (จอไม่ขึ้น) / DP (คอนเนกเตอร์ผิด → จอดำ)
- `disable-agdc`, `AAPL,GfxYTile`, `agdpmod=ignore`, `igfxfcms=1`
- ลบ `framebuffer-fbmem`/`stolenmem` → ค้าง
- OCLP 2.5.1 → "No Root Patches required"
- SMBIOS `iMac18,1` → จอดำ (รุ่น all-in-one ไม่ตรงกับเครื่อง)

## 5) บทเรียนการทำงาน (สำคัญสำหรับครั้งหน้า)
- เครื่องนี้มี **2 EFI** ที่ผู้ใช้สลับเองได้ → ฝัง **marker** ใน boot-args ทุกครั้ง:
  `espm=efi` = EFI หลัก (disk0s1) · `espm=boot` = EFI สำรอง (disk0s2 `BOOT`)
- **ตรวจ marker ก่อนสรุปผลทุกครั้ง:** `nvram boot-args | grep -o 'espm=[a-z]*'`
- ตรวจผลที่เชื่อถือได้: `system_profiler SPDisplaysDataType` · `kmutil showloaded | grep -iE 'lilu|whatevergreen|KBL'` · `nvram boot-args`
- ⚠️ ESP ถูก unmount ทุกครั้งหลังรีบูต → ต้อง `sudo diskutil mount disk0s1` ก่อนแก้ไฟล์

## 6) ไฟล์สำรอง / ที่เก็บของ
| ที่ | อะไร |
|---|---|
| `/Volumes/EFI/EFI.bak-v17-20260922-013655` | EFI หลักก่อนคืนค่าชุดที่ใช้ได้ |
| `/Volumes/EFI/EFI.backup-20260922-011838` | EFI หลัก (ชุดทดลองเก่า) |
| `/Volumes/BOOT/EFI.backup-20260922-011435` | EFI สำรอง (ก่อนแก้) |
| `OC/Kexts/_old-kexts/` | Lilu/WG เวอร์ชันทดลอง (1.6.9 / 1.6.8 / เดิม) |
| `OC/config.plist.bak*`, `config.plist.presafe-*` | ประวัติ config ทุกเวอร์ชัน |
| workspace `.openclaw/tmp/gui/` | สคริปต์ (`mkconfig.py`, `mkvariant.py`, `mkedidoverride.py`) + config ทุกเวอร์ชัน + `override/EDID.orig.hex` |

## 7) คำแนะนำต่อ
- ถ้าจะอัปเดต macOS ในอนาคต ให้ตรวจ **SMBIOS `MacPro7,1`** และ **`igfxonln=1`** ว่ายังอยู่ (สองตัวนี้คือหัวใจ)
- ถ้าจะอัป OpenCore: ใช้ชุด VERSION เดียวกันทั้งชุด (OpenCore.efi + BOOTx64.efi + drivers) และอัป Lilu ให้ ≥ ที่ WhateverGreen ต้องการ
- สำหรับ Theme: `Resources/Image/Acidanthera/GoldenGate` มีอยู่แล้ว; ธีมอื่น (Chardonnay/Syrah) โหลด `Resources` จาก OpenCorePkg มาเพิ่มได้
