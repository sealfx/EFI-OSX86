# วิธีใช้งาน / How to use

คู่มือนี้สำหรับคนที่โหลด EFI จาก repo นี้ไปใช้กับเครื่องของตัวเอง
**อ่านให้ครบก่อนแตะ EFI ของเครื่อง** เพราะเขียนผิดพลาดอาจทำให้เครื่องบูตไม่ขึ้น

---

## 0) ก่อนเริ่ม — ทำความเข้าใจก่อน

| ข้อ | ทำไม |
|---|---|
| EFI ในนี้ **ผูกกับฮาร์ดแวร์รุ่นนั้น** | เครื่องต่างรุ่นใช้แทนกันได้ไม่เสมอ ต้องปรับ `config.plist` เอง |
| EFI ในนี้ **ไม่ใช่คู่มือติดตั้ง macOS** | เป็นเพียงชุดไฟล์บูต การสร้าง USB ติดตั้งให้อ่าน [Dortania OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/) |
| ทุกไฟล์มี md5 | ตรวจก่อนใช้ทุกครั้งเพื่อกันไฟล์เสีย/ถูกแก้ |
| **ห้ามใช้ serial ที่ติดมากับไฟล์** | ถ้าซ้ำกับคนอื่นจะเกิดปัญหา iCloud / iMessage / FaceTime |

---

## 1) เลือกชุดให้ตรงเครื่อง

ดูตารางใน [`README.md`](../README.md) หรือ [`HARDWARE-MATRIX.md`](./HARDWARE-MATRIX.md)
แล้วเข้าโฟลเดอร์ `configs/<เครื่อง>/<macOS>/` ที่ต้องการ — ตรวจว่า **CPU / GPU / ชิปเสียง / เน็ต** ตรงกับเครื่องคุณ

## 2) ตรวจ md5 ของไฟล์ที่โหลดมา

```bash
# ดูค่าที่ควรได้
grep '<ชื่อไฟล์>.zip' MANIFEST.md5

# เทียบกับไฟล์ที่โหลดมา
md5 -q '<ชื่อไฟล์>.zip'          # macOS
md5sum '<ชื่อไฟล์>.zip'          # Linux
```
ถ้าไม่ตรง **อย่าใช้** — โหลดใหม่

## 3) สำรอง EFI เดิมของเครื่องก่อน

```bash
diskutil list                      # หา EFI ของดิสก์ที่บูต (ปกติ disk0s1)
sudo diskutil mount disk0s1
ls /Volumes/EFI/EFI

sudo cp -R /Volumes/EFI/EFI "/Volumes/EFI/EFI.backup-$(date +%Y%m%d-%H%M%S)"
```

## 4) คัดลอก EFI ใหม่ทับ

```bash
unzip '<ชื่อไฟล์>.zip' -d /tmp/new-efi
# โครงสร้างใน zip: <ชื่อชุด>/BOOT/ และ <ชื่อชุด>/OC/
sudo cp -R /tmp/new-efi/<ชื่อชุด>/* /Volumes/EFI/EFI/
```

**หมายเหตุ:** หลังรีบูต EFI มักถูก unmount เอง → ต้อง `sudo diskutil mount disk0s1` ทุกครั้งก่อนแก้ไฟล์

## 5) สร้าง SMBIOS ของตัวเอง (สำคัญที่สุด)

1. เปิด `EFI/OC/config.plist` (ใช้ ProperTree หรือ OpenCore Configurator)
2. หา `PlatformInfo > Generic`
3. ใช้ [GenSMBIOS](https://github.com/corpnewt/GenSMBIOS) สร้างค่าใหม่สำหรับรุ่นที่ repo นี้ระบุ
   (เช่น Dell Sequoia ใช้ `MacPro7,1`) แล้วใส่ `SystemSerialNumber`, `MLB`, `SystemUUID`
4. **ห้ามลอก serial ที่มีอยู่ในไฟล์**

## 6) Reset NVRAM

ตอนบูต กด Space ที่หน้า OpenCore Picker → เลือก `Reset NVRAM` (ถ้าชุดนั้นมี `ResetNvramEntry.efi`)
หรือกด `Cmd+Opt+P+R` ขณะบูต

## 7) ถ้าบูตไม่ขึ้น

1. เพิ่ม boot-arg `-v` เพื่อดูข้อความ verbose แล้วถ่ายรูปไว้
2. ใช้ `-x` (safe mode) ลองแยกว่าเป็นปัญหา kext หรือ patch
3. เปิด `Misc > Debug > Target = 67` เพื่อเขียนไฟล์ log ลง EFI
4. ถ้ามีจอแต่สีเพี้ยน/ดำ → ดูหัวข้อ "บทเรียน" ของชุดที่ตรงเครื่อง (เช่น Dell Sequoia: SMBIOS + `igfxonln=1`)

---

## 📌 บทเรียนที่มีค่าจากชุดต่าง ๆ

| ชุด | อาการ | ต้นเหตุ / วิธีแก้ |
|---|---|---|
| Dell Precision T3420 (Sequoia) | สีเพี้ยน ฟ้า↔ส้ม, Framebuffer Depth 30-bit | SMBIOS `iMac18,3` ผิด → เปลี่ยนเป็น **`MacPro7,1`** |
| Dell Precision T3420 (Sequoia) | จอค้าง/ดับหลังเข้าหน้าจอ เหลือแต่ Cursor | สถานะจอถูกตัดเป็น offline → boot-arg **`igfxonln=1`** |
| Dell Precision T3420 (Sequoia) | ทดสอบแล้ว **ไม่ใช่สาเหตุ** | เวอร์ชัน OpenCore/Lilu/WhateverGreen, EDID override, `agdpmod=ignore`, OCLP |

รายละเอียดทั้งหมดดูใน [`configs/dell-precision-t3420/macos-sequoia-15.7/notes/EFI-Dell-Precision-3420.md`](../configs/dell-precision-t3420/macos-sequoia-15.7/notes/EFI-Dell-Precision-3420.md)

---

## 🔗 แหล่งอ้างอิงมาตรฐาน

- Dortania — OpenCore Install Guide: https://dortania.github.io/OpenCore-Install-Guide/
- OpenCorePkg: https://github.com/acidanthera/OpenCorePkg
- GenSMBIOS: https://github.com/corpnewt/GenSMBIOS
- รายการ kext/ที่มาใน repo นี้: [`CREDITS.md`](./CREDITS.md)
