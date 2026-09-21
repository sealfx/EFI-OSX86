# สรุปงานฉบับสมบูรณ์: Dell (i7-7700 / Intel HD 630) + macOS Sequoia 15.7.9 — EFI / กราฟิก / ธีม / พอร์ต

_อัปเดตล่าสุด: 2026-09-22 04:40 (+07)_

## 1) ผลลัพธ์สุดท้าย
| หัวข้อ | สถานะ |
|---|---|
| จอแสดงผล | ✅ **1 จอ** ใช้งานได้ (DP → DELL) — **สลับไปพอร์ต DP อีกช่องก็ใช้ได้** ✓ |
| **สีถูกต้อง** | ✅ **แก้สำเร็จ** (สาเหตุคือ SMBIOS) |
| iGPU acceleration | ✅ 1536 MB · Metal 3 · ลื่น |
| ธีม OpenCore | ✅ GoldenGate (ไม่แตะ `OpenCore.efi`) |
| 2 จอ (HDMI + DP) | ❌ ทำไม่ได้บน BIOS/การเดินสายของเครื่องนี้ (ทดลองครบแล้ว — ดูข้อ 4) |
| พอร์ต USB 3.0 | ❌ macOS ไม่สร้างพอร์ต SuperSpeed (ดูข้อ 5) |

## 2) กุญแจสำคัญ (root cause) ที่แก้สำเร็จ
| อาการ | สาเหตุจริง | วิธีแก้ |
|---|---|---|
| สีเพี้ยน ฟ้า↔ส้ม / จอเขียว / depth 30-bit | **SMBIOS (board-id) `iMac18,3`** | เปลี่ยนเป็น **`MacPro7,1`** → สีถูก |
| จอดับ/ค้างหลังเข้าหน้าจอ | สถานะจอ offline | boot-arg **`igfxonln=1`** |

## 3) EFI 2 ชุด (ใช้งานจริง)
| | EFI หลัก (`/Volumes/EFI`) | EFI สำรอง (`/Volumes/BOOT`) |
|---|---|---|
| marker | `espm=efi` | `espm=boot` |
| config | **HD620 + `con1-type=HDMI` + `con2-type=DP`** (แบบ `-type` ธรรมดา — **DP ขึ้น ✓**) | **ชุดเดียวกันเป๊ะ** (ต่างแค่ marker) ✓ |
| OpenCore / Lilu / WG | 1.0.8 / 1.7.2 / 1.7.0 | เท่ากัน |
| SMBIOS / args | MacPro7,1 · `igfxonln=1` | เท่ากัน |
| ธีม | GoldenGate | GoldenGate |

> ตรวจว่าบูทจากตัวไหน: `nvram boot-args | grep -o 'espm=[a-z]*'`

## 4) แผนผังพอร์ตกราฟิกของเครื่องนี้ (ค้นพบจริง)
- macOS สร้างคอนเนกเตอร์ 3 ตัว → **port 5, 6, 7**
- **พอร์ต DP ของเครื่องใช้ได้ ✓** (จอ DELL ขึ้น — สลับไปพอร์ต DP อีกช่องก็ยังใช้ได้)
- **พอร์ต HDMI ของเครื่อง: ขับด้วย macOS ไม่ได้** — ลอง type HDMI ที่ port 5 และ port 7 แล้วไม่ขึ้นทั้งคู่ (น่าจะเป็นข้อจำกัด BIOS/VBT)
- **สิ่งที่ทำให้จอดับ: `-alldata` + การประกาศ 3 คอนเนกเตอร์** ⇒ กลับมาใช้แบบ `-type` ธรรมดา (con1=HDMI, con2=DP) แล้วเสถียร ✓
- ทดลอง 2 จอครบทุกมุมแล้ว: โปรไฟล์ desktop/HD620, SMBIOS iMac18.1/MacPro7.1, `-alldata` 3 แบบ ⇒ **ได้ 1 จอเสมอ**
- ตัวเลือกที่ยังไม่ได้ลอง (ถ้าอยากสู้ต่อในอนาคต): SMBIOS **Macmini8,1** (รุ่นที่ iGPU ขับจอเองโดยไม่มี dGPU)

## 5) ปัญหา USB 3.0 (สรุปไว้ทำต่อ)
- macOS สร้างพอร์ต **USB2 (XHCI) 15 พอร์ต** แต่ **USB3 SuperSpeed = 0** ⇒ อุปกรณ์ USB3 (ฮาร์ดดิสก์) ไม่ถูกตรวจพบบนพอร์ต 3.0
- สาเหตุ: ข้อจำกัด 15 พอร์ต/คอนโทรลเลอร์ + `UTBDefault.kext` **ไม่มีข้อมูลพอร์ต** (placeholder เปล่า)
- วิธีแก้: สร้าง **USB port map จริง** (USBToolBox) แล้วแทน `UTBDefault.kext` — ต้อง map บนเครื่องที่เห็นพอร์ตครบ (Windows) หรือ map มือจาก ioreg
- ชั่วคราว: ต่ออุปกรณ์ USB3 เข้าพอร์ต USB2 (สีดำ) จะใช้ได้ (ความเร็ว USB2)

## 6) สิ่งที่ทดลองแล้ว **ไม่ใช่สาเหตุ** (อย่าลองซ้ำ)
- เวอร์ชัน OpenCore/Lilu/WG (ทดสอบ 1.7.2/1.7.0 → 1.6.9 → 1.6.8 + OC 1.0.7/1.0.6)
- EDID override ที่ `/Library/Displays` (macOS ไม่อ่าน)
- `-igfxvesa`, DVI/DP connector typing รอบแรกๆ, `disable-agdc`, `AAPL,GfxYTile`, `agdpmod=ignore`, `igfxfcms=1`, ลบ memory patch (ค้าง), OCLP 2.5.1 ("No Root Patches required"), `-igfxonlnfbs`

## 7) ไฟล์/ที่เก็บ
| ที่ | อะไร |
|---|---|
| `OC/config.plist.bak*` (EFI หลัก) | ประวัติ config ทุกเวอร์ชัน (bak32 = ชุด DP ✓, bak33 = ปัจจุบัน) |
| `/Volumes/EFI/EFI.backup-*`, `EFI.bak-v17-*` | สำรอง EFI ทั้งชุด |
| `/Volumes/BOOT/EFI.backup-20260922-011435` | สำรอง EFI สำรอง |
| `OC/Kexts/_old-kexts/` | Lilu/WG เวอร์ชันทดลอง |
| workspace `.openclaw/tmp/gui/` | สคริปต์ + config ทุกเวอร์ชัน + EDID ต้นฉบับ |

## 8) หมายเหตุสำหรับอนาคต
- **อย่าลืม 2 ตัวนี้ถ้าอัป macOS**: SMBIOS `MacPro7,1` และ boot-arg `igfxonln=1` (หัวใจของ setup นี้)
- อัป OpenCore: ใช้ drivers ชุด version เดียวกัน (OpenCore.efi + BOOTx64.efi + drivers)
