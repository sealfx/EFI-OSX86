# EFI-OSX86

รวม EFI Hackintosh (x86 / OSX86) ของเครื่องหลายรุ่นไว้ในที่เดียว แต่ละชุดแยกตาม **เครื่อง × เวอร์ชัน macOS** พร้อม md5 ทุกไฟล์

A consolidated collection of Hackintosh EFI configurations, organized by **machine × macOS version**, each with verified md5 checksums.

## สารบัญ / Index

| เครื่อง / Machine | macOS | CPU | GPU | Audio | LAN |
|---|---|---|---|---|---|
| [GIGABYTE GA-H61M-DS2](configs/gigabyte-ga-h61m-ds2/macos-catalina-10.15.4/README.md) | Catalina 10.15.4 | Intel Core i3 @ 3.20GHz | AMD Radeon RX570 8GB | Realtek ALC887 | Realtek 8111 |
| [GIGABYTE GA-H61M-DS2](configs/gigabyte-ga-h61m-ds2/macos-high-sierra-10.13.6/README.md) | High Sierra 10.13.6 | Intel Core i3 @ 3.20GHz | AMD Radeon RX570 8GB | Realtek ALC887 | Realtek 8111 |
| [Dell Precision T3420](configs/dell-precision-t3420/macos-high-sierra-10.13.6/README.md) | High Sierra 10.13.6 | Intel Core i7-7700 (4C/8T, 3.6GHz, Turbo 4.20GHz, 8MB) | NVIDIA Quadro K1200 4GB (4 x mDP, Low Profile) | - | - |
| [Dell Precision T3420](configs/dell-precision-t3420/macos-sierra-10.12.6/README.md) | Sierra 10.12.x | Intel Core i7-7700 (Quad Core, 8MB Cache, 3.6GHz, Turbo up to 4.20GHz) | NVIDIA Quadro K1200 4GB (4 x mDP, Low Profile) | Integrated (Onboard) | - |
| [Dell Precision T7450 AIO (23.8" All-in-One)](configs/dell-precision-t7450-aio/macos-high-sierra-10.13.6/README.md) | High Sierra 10.13.6 | Intel Core i5-7500 | Intel HD Graphics 630 (ใช้ได้) | - | - |
| [HP Pavilion 24-b212d Z8G27AA#AKL (23.8" All-in-One)](configs/hp-pavilion-24-b212d/macos-high-sierra-10.13.6/README.md) | High Sierra 10.13.6 | Intel Core i5-7400T 2.4GHz | Intel HD Graphics 630 — ใช้งานได้ | - | - |
| [Dell Precision T3420 (i7-7700 + iGPU)](configs/dell-precision-t3420/macos-sequoia-15.7/README.md) | Sequoia 15.7.9 (24G830) | Intel Core i7-7700 | Intel HD Graphics 630 (iGPU) — เร่งความเร็วได้ 1536 MB, Metal 3 | - | - |
| [Apple Mac Pro (Late 2013)](configs/macpro-late-2013/macos-sequoia-15.x/README.md) | Sequoia 15.x — อ้างจากชื่อไฟล์ (ไม่ได้ระบุเลขเวอร์ชันย่อย) | - | - | - | - |

## โครงสร้าง / Layout

```
EFI-OSX86/
├── configs/<machine>/<macos-version>/   # EFI zip + screenshots + README
├── shared/opencore-any/                  # EFI OpenCore ทั่วไป
├── docs/                                 # ตารางฮาร์ดแวร์ + กติกาการแก้ไข
├── upstream/                             # สำเนาเอกสารต้นฉบับ (traceability)
├── tools/                                # sync / verify / patch
└── MANIFEST.md5                          # md5 ของทุกไฟล์
```

## ใช้งานเร็ว / Quick start

```bash
# ตรวจความถูกต้องของทุกไฟล์
bash tools/verify_md5.sh

# ดึงต้นทางล่าสุดจาก GitHub แล้วสร้างใหม่ (idempotent)
bash tools/sync.sh
```

## หมายเหตุ / Notes

- ไฟล์ EFI เก็บเป็น zip ต้นฉบับ **ไม่แตกและไม่บีบอัดใหม่** เพื่อรักษาไบต์เดิม
- ทุกไฟล์มี md5 บันทึกใน [`MANIFEST.md5`](./MANIFEST.md5)
- EFI เหล่านี้มาจากเครื่องจริงที่เคยใช้งานได้ ณ เวอร์ชัน macOS ที่ระบุ การนำไปใช้กับเครื่องอื่นต้องปรับ `config.plist` / SMBIOS เอง
