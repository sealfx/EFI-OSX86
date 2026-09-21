# ตรวจสอบ "2 จอ" กับเครื่องจริง — บันทึกผล

_ตรวจเมื่อ 2026-09-22 05:05 (+07) · วิธี: อ่านอย่างเดียว (system_profiler / ioreg / config.plist)_

## คำถามที่ต้องตอบ
เอกสาร `EFI-Dell-Precision-3420.md` (อัปเดต 2026-09-22 04:40) เขียนว่า
"2 จอ (HDMI + DP) ❌ ทำไม่ได้" แต่เจ้าของเครื่องแจ้งว่าใช้ได้ 2 จอ → ต้องตรวจจริง

## ผลการตรวจ (observed)

| # | จอ | ความละเอียด | Main | Mirror | Online | Adapter Type |
|---|---|---|---|---|---|---|
| 1 | Monitor | 1920×1080 @ 60Hz | – | Off | Yes | – |
| 2 | DELL E1914H | 1366×768 @ 60Hz | Yes | Off | Yes | Analog VGA or Analog Over DVI-I |

- `system_profiler SPDisplaysDataType` → **Displays: 2 รายการ** (mirror = Off ทั้งคู่, online = Yes ทั้งคู่)
- จำนวน EDID ที่ระบบอ่านได้: **2**
- `ioreg -c AppleIntelFramebuffer`:
  - `port-number = 5` · `connector-type = 00080000` (HDMI) → มี `IODisplayConnect` + `AppleDisplay` (active)
  - `port-number = 6` · `connector-type = 00040000` (DP) → มี `IODisplayConnect` + `AppleDisplay` (active)
- ค่าใน config ที่บูตอยู่ (`/Volumes/EFI/EFI/OC/config.plist` และ `/Volumes/BOOT/EFI/OC/config.plist` — เหมือนกัน):
  ```
  framebuffer-con1-enable = 01000000   framebuffer-con1-type = 00080000  (HDMI)
  framebuffer-con2-enable = 01000000   framebuffer-con2-type = 00040000  (DP)
  AAPL,ig-platform-id     = 00001659   framebuffer-stolenmem = 00003001
  ```
- boot-args ตอนตรวจ: `keepsyms=1 debug=0x100 alcid=11 -no_compat_check -wegnoegpu igfxonln=1 espm=efi`
  (บูตจาก **EFI หลัก**; ชุดที่อัปโหลดเข้า repo เป็น EFI สำรอง `espm=boot` แต่ config เหมือนกัน)
- `Framebuffer Depth` = **30-Bit Color (ARGB2101010)** ทั้ง 2 จอ — แต่สีถูกต้อง
  ⇒ **30-bit ไม่ใช่สาเหตุของสีเพี้ยน** (สาเหตุคือ SMBIOS เดิม `iMac18,3`)

## สรุป
**2 จอพร้อมกันใช้ได้จริง** — พอร์ต HDMI (port 5, ผ่านอะแดปเตอร์ไปจอ DELL E1914H)
และพอร์ต DP (port 6, จอ 1920×1080)

ข้อความ "❌ 2 จอทำไม่ได้" ใน `EFI-Dell-Precision-3420.md` **ล้าสมัย** ให้ถือผลการตรวจนี้เป็นหลัก

> ข้อจำกัดของหลักฐาน: ระบบมองเห็นจอ 2 ตัวและคอนเนกเตอร์ทั้งสอง active
> แต่ไม่ได้พิสูจน์ด้วยสายตาว่าภาพออกทั้งสองจอพร้อมกันจริง (ผู้ใช้ยืนยันว่าได้)
