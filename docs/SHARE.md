# ข้อความสำหรับแชร์ / Share templates

คัดลอกไปใช้ได้เลย — แนะนำให้แก้ชื่อ/รายละเอียดเครื่องให้ตรงกับที่คุณต้องการเน้น

---

## 🇹🇭 ภาษาไทย (Facebook / กลุ่ม Hackintosh ไทย)

> **รวม EFI Hackintosh ไว้ที่เดียว — sealfx/EFI-OSX86**
>
> ผมรวบรวม EFI ที่เคยใช้งานได้จริงบนเครื่องของผม มาไว้ใน repo เดียว จัดเป็นโฟลเดอร์ตามเครื่อง × เวอร์ชัน macOS
> ทุกไฟล์มี md5 ให้ตรวจ มี CI ตรวจความถูกต้องอัตโนมัติ
>
> เครื่องที่มี: Gigabyte GA-H61M-DS2 (Catalina 10.15.4 / High Sierra 10.13.6), Dell Precision T3420
> (High Sierra / Sierra / **Sequoia 15.7.9**), Dell T7450 AIO, HP Pavilion 24-b212d, **Mac Pro Late 2013 (Sequoia)**
>
> ที่น่าสนใจสุดคือชุด **Dell + Sequoia**: จุดที่ทำให้สำเร็จคือเปลี่ยน SMBIOS เป็น `MacPro7,1`
> (แก้สีเพี้ยน ฟ้า↔ส้ม) และ boot-arg `igfxonln=1` (แก้จอค้าง/ดับหลังเข้าหน้าจอ) — เขียนไว้ละเอียดใน repo
>
> 👉 https://github.com/sealfx/EFI-OSX86
> ⚠️ EFI ผูกกับฮาร์ดแวร์รุ่นนั้น ๆ และห้ามใช้ serial ที่แถมมา ให้สร้าง SMBIOS ของตัวเองก่อนใช้
> (repo เป็นแค่ชุดไฟล์บูต ไม่ใช่คู่มือติดตั้ง macOS)

---

## 🇬🇧 English (r/hackintosh, InsanelyMac, tonymacx86)

> **[EFI] Consolidated Hackintosh EFI collection — sealfx/EFI-OSX86**
>
> I collected the EFIs that actually booted on my machines into a single repo, organized by
> machine × macOS version, with md5 checksums for every file and CI that verifies them on each push.
>
> Machines included: Gigabyte GA-H61M-DS2 (Catalina 10.15.4 / High Sierra 10.13.6),
> Dell Precision T3420 (High Sierra / Sierra / **Sequoia 15.7.9**), Dell T7450 AIO,
> HP Pavilion 24-b212d, **Mac Pro Late 2013 (Sequoia, OCLP-style)**.
>
> Most interesting is the Dell + Sequoia set: the fix was switching SMBIOS to `MacPro7,1`
> (color inversion / 30-bit framebuffer) plus boot-arg `igfxonln=1` (black screen after boot).
> There's a troubleshooting write-up with what was tested and ruled out.
>
> 👉 https://github.com/sealfx/EFI-OSX86
>
> ⚠️ These EFIs are hardware-specific. Do **not** use the bundled SMBIOS serial — generate your own.
> This is a boot-file collection, not an install guide.

---

## ข้อควรระวังเวลาโพสต์

- **ห้ามโพสต์เป็นลิงก์เปล่า** — หลายชุมชนแบน ลิงก์ลอย ให้ใส่บริบท/รายละเอียดตามตัวอย่างข้างบน
- อ่านกฎของแต่ละชุมชนก่อน (r/hackintosh มีกฎเรื่อง self-promotion และการแปะ EFI)
- อย่าใช้คำว่า "ใช้ได้ทุกเครื่อง" — EFI ผูกกับฮาร์ดแวร์
- ถ้ามีคนถาม ให้ชี้ไปที่ [`HOW-TO-USE.md`](./HOW-TO-USE.md) และ [`TROUBLESHOOTING.md`](./TROUBLESHOOTING.md)
