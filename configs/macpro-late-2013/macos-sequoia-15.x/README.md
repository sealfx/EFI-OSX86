# Apple Mac Pro (Late 2013) — macOS Sequoia 15.x

> Apple Mac Pro (Late 2013) — macOS Sequoia 15.x

ที่มา: ไฟล์ที่อัปโหลดโดยเจ้าของ repo (local upload) — ข้อมูลสกัดจาก `OC/config.plist` และรายการไฟล์ใน zip จริง

## ข้อมูลเครื่อง / Hardware

| รายการ | ค่า |
|---|---|
| Machine | Apple Mac Pro (Late 2013) |
| SMBIOS | ไม่กำหนดทับ — `PlatformInfo/Generic` ว่าง (ใช้ค่าเดิมของเครื่องจริง) |
| boot-args | `keepsyms=1 debug=0x100 -lilubetaall ipc_control_port_options=0 -nokcmismatchpanic` |
| Drivers | OpenRuntime.efi, OpenCanopy.efi, OpenLinuxBoot.efi, ResetNvramEntry.efi |
| Kext | 15 รายการ: Lilu, RestrictEvents, NVMeFix, AMFIPass, AirportBrcmFixup, IOSkywalkFamily, IO80211FamilyLegacy (+AirPortBrcmNIC), CryptexFixup, RSRHelper, AppleIntelCPUPowerManagement(+Client), USB-Map, ECM-Override, CatalinaIntelI210Ethernet, AutoPkgInstaller |
| ธีม / Theme | GoldenGate (`PickerMode=External`) |
| macOS | Sequoia 15.x — อ้างจากชื่อไฟล์ (ไม่ได้ระบุเลขเวอร์ชันย่อย) |

## ไฟล์ EFI

| ไฟล์ | md5 |
|---|---|
| [`EFI-Macpro-Late2013-Sequoia.zip`](./EFI-Macpro-Late2013-Sequoia.zip) | `705a1846e368b099fd17e5398136b6d2` |

## ข้อสังเกต / Observations

- **ไม่มีเอกสารประกอบในชุดที่อัปโหลด** — ข้อมูลในหน้านี้สกัดจาก `OC/config.plist` และรายการไฟล์ใน zip จริง ไม่ได้คัดลอกจากที่อื่น
- ชุดนี้ออกแบบสำหรับ **เครื่อง Mac จริง** (ไม่ตั้ง SMBIOS ทับ) และมีโฟลเดอร์ `APPLE/CACHES` พร้อม kext สาย legacy (`CryptexFixup`, `RSRHelper`, `AutoPkgInstaller`, `IO80211FamilyLegacy`) → ลักษณะของชุดที่ทำด้วย **OpenCore Legacy Patcher (OCLP)**
- zip ติดไฟล์ metadata ของ macOS (`__MACOSX/`, `._*`, `.DS_Store`) มาด้วย — เก็บตามต้นฉบับ
- ไม่พบ `SystemProductName` ใน config จึงยืนยันรุ่นเครื่องจากไฟล์ไม่ได้ นอกจากชื่อไฟล์ที่ระบุ Mac Pro Late 2013

## วิธีใช้ / Usage

1. ดาวน์โหลดไฟล์ EFI zip ในโฟลเดอร์นี้
2. แตก zip และคัดลอกโฟลเดอร์ `EFI/` ลง EFI System Partition (ESP) ของเครื่อง
3. ปรับ `config.plist` (SMBIOS / serial) ให้ตรงกับเครื่องของคุณก่อนใช้งาน
4. ตรวจสอบ md5 ของ zip ให้ตรงกับตารางด้านบนก่อนใช้

---

_ไฟล์นี้สร้างโดย `tools/build.py` — แก้ไขที่ generator ไม่ใช่แก้ไฟล์นี้ตรง ๆ_
