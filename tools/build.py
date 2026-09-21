#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EFI-OSX86 builder — สร้าง/อัปเดต repo รวม EFI จากต้นทาง GitHub sealfx

Usage:
  python3 tools/build.py              # build tree + MANIFEST.md5 จาก upstream ที่มีอยู่
  python3 tools/build.py --list-repos # พิมพ์ชื่อ repo ต้นทาง (ใช้โดย sync.sh)
"""
from __future__ import annotations
import datetime, hashlib, json, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)                 # .../EFI-OSX86
ROOT = os.path.dirname(REPO)                 # workspace root
UP = os.path.join(ROOT, "_recon", "upstream")
OWNER = "sealfx"


def md5(path: str) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def norm(name: str) -> str:
    """จัดชื่อไฟล์: ช่องว่าง -> _"""
    return name.replace(" ", "_")


ENTRIES = [
    dict(
        vendor="gigabyte-ga-h61m-ds2",
        os_slug="macos-catalina-10.15.4",
        src="GIGABIYE-GA-H61M-DS2-Catalina",
        branch="master",
        title_th="Gigabyte GA-H61M-DS2 — macOS Catalina 10.15.4",
        title_en="Gigabyte GA-H61M-DS2 — macOS Catalina 10.15.4",
        hw=[
            ("Mainboard / เมนบอร์ด", "GIGABYTE GA-H61M-DS2"),
            ("CPU", "Intel Core i3 @ 3.20GHz"),
            ("RAM", "16GB (2 x 8GB) DDR3"),
            ("GPU", "AMD Radeon RX570 8GB"),
            ("Audio / เสียง", "Realtek ALC887"),
            ("LAN / เน็ตเวิร์ก", "Realtek 8111"),
            ("macOS", "Catalina 10.15.4"),
        ],
        efi=[("EFI-GA-H61M-DS2-Catalina.zip", "7dd628bc6edd2749a92029500561eed9")],
        screenshots=["Screen_Audio_Device.png", "Screen_GFX_Readion_RX570.png",
                     "Screen_Network.png", "Screen_Osx_Catalina10.15.4.png"],
        notes=[],
        observations=[],
    ),
    dict(
        vendor="gigabyte-ga-h61m-ds2",
        os_slug="macos-high-sierra-10.13.6",
        src="GIGABIYE-GA-H61M-DS2-Hight-Sierra",
        branch="master",
        title_th="Gigabyte GA-H61M-DS2 — macOS High Sierra 10.13.6",
        title_en="Gigabyte GA-H61M-DS2 — macOS High Sierra 10.13.6",
        hw=[
            ("Mainboard / เมนบอร์ด", "GIGABYTE GA-H61M-DS2"),
            ("CPU", "Intel Core i3 @ 3.20GHz"),
            ("RAM", "16GB (2 x 8GB) DDR3"),
            ("GPU", "AMD Radeon RX570 8GB"),
            ("Audio / เสียง", "Realtek ALC887"),
            ("LAN / เน็ตเวิร์ก", "Realtek 8111"),
            ("macOS", "High Sierra 10.13.6"),
        ],
        efi=[("EFI-GA-H61M-DS2-Hight-Sierra.zip", "ba8ee8af02f4ca4d277e7bc2f9c3909b")],
        screenshots=["Screen_Audio.png", "Screen_GFX_Readion_RX570.png",
                     "Screen_Network.png", "Screen_Osx_Hightsierra10.13.6.png"],
        notes=[],
        observations=[],
    ),
    dict(
        vendor="dell-precision-t3420",
        os_slug="macos-high-sierra-10.13.6",
        src="DELL-Precision-T3420-Hight-Sierra",
        branch="master",
        title_th="Dell Precision T3420 — macOS High Sierra 10.13.6",
        title_en="Dell Precision T3420 — macOS High Sierra 10.13.6",
        hw=[
            ("Workstation", "Dell Precision T3420"),
            ("CPU", "Intel Core i7-7700 (4C/8T, 3.6GHz, Turbo 4.20GHz, 8MB)"),
            ("Chipset", "Intel C236"),
            ("RAM", "16GB (1 x 16GB) DDR4 2400MHz UDIMM Non-ECC"),
            ("GPU", "NVIDIA Quadro K1200 4GB (4 x mDP, Low Profile)"),
            ("Storage", "256GB SSD"),
            ("macOS", "High Sierra 10.13.6"),
        ],
        efi=[("EFI_DELL_Precision_T3420_Hight_Sierra.zip", "b0bedbcdf7e93a5780477dc8a168aeef")],
        screenshots=["Screen_Audio_AlC255.png", "Screen_Dell Precision T3420.png",
                     "Screen_Ethernet.png", "Screen_Hight_Sierra_10.13.6.png",
                     "Screen_Nvidia Quadro K1200.png"],
        notes=[],
        observations=[],
    ),
    dict(
        vendor="dell-precision-t3420",
        os_slug="macos-sierra-10.12.6",
        src="DELL-Precision-T3420-Sierra",
        branch="master",
        title_th="Dell Precision T3420 — macOS Sierra 10.12.x",
        title_en="Dell Precision T3420 — macOS Sierra 10.12.x",
        hw=[
            ("Workstation", "Dell Precision T3420"),
            ("CPU", "Intel Core i7-7700 (Quad Core, 8MB Cache, 3.6GHz, Turbo up to 4.20GHz)"),
            ("Chipset", "Intel C236"),
            ("RAM", "16GB (1 x 16GB) DDR4 2400MHz UDIMM Non-ECC"),
            ("GPU", "NVIDIA Quadro K1200 4GB (4 x mDP, Low Profile)"),
            ("Optical drive", "DVD-/+RW 8x"),
            ("Storage", "256GB SSD"),
            ("Audio / Sound", "Integrated (Onboard)"),
            ("Wireless / BT", "None (ไม่มี)"),
            ("macOS", "Sierra 10.12.x"),
        ],
        efi=[("EFI_DELL_Precision_T3420_Sierra.zip", "4990017221fc3b6a27bcb962d6b94669")],
        screenshots=["Screen_Audio Device.png", "Screen_Dell Precision T3420.png",
                     "Screen_Ethernet Device.png", "Screen_Nvidia Quadro K1200.png",
                     "Screen_macOS Sieera.png"],
        notes=["Dell Workstation T3420.txt"],
        observations=[
            "เวอร์ชัน macOS ไม่ตรงกันในเอกสารต้นฉบับ: README ของ repo เขียน **Sierra 10.12.3** "
            "แต่ description ของ repo และชื่อ screenshot ระบุ **10.12.6** — ยังไม่ได้ยืนยันว่าอันไหนถูก",
        ],
    ),
    dict(
        vendor="dell-precision-t7450-aio",
        os_slug="macos-high-sierra-10.13.6",
        src="DELL-Precision-T7450-AIO",
        branch="master",
        title_th="Dell Precision T7450 AIO — macOS High Sierra 10.13.6",
        title_en="Dell Precision T7450 AIO — macOS High Sierra 10.13.6",
        hw=[
            ("Machine", 'Dell Precision T7450 AIO (23.8" All-in-One)'),
            ("CPU", "Intel Core i5-7500"),
            ("RAM", "16GB DDR4"),
            ("Storage", "256GB SSD (+ NVMe M.2 Samsung ตาม screenshot)"),
            ("Display", '23.8" FHD Touch'),
            ("GPU", "Intel HD Graphics 630 (ใช้ได้)"),
            ("macOS", "High Sierra 10.13.6"),
        ],
        efi=[("EFI_DELL_Precision_T7450_AIO.zip", "e61585b43b9fe13365205e386cb756b0")],
        screenshots=["Screen_Audio.png", "Screen_Dell_Precision_7450_Spec.png",
                     "Screen_GFX_HD_630.png", "Screen_MacOs_Hight_Sierra_10.13.6.png",
                     "Screen_Nvme_M2_Sansung.png"],
        notes=[],
        observations=[
            'Readme ต้นฉบับเขียนชื่อรุ่นว่า "DELL OptiPlex T7450 AIO" แต่ชื่อ repo และชื่อไฟล์ EFI '
            'เป็น "DELL_Precision_T7450_AIO" — เก็บชื่อเดิมไว้ทั้งคู่ ไม่ได้แก้ให้ตรงกัน',
        ],
    ),
    dict(
        vendor="hp-pavilion-24-b212d",
        os_slug="macos-high-sierra-10.13.6",
        src="HP-Pavilion-24-b212d-Z8G27AA-AKL-AIO",
        branch="master",
        title_th="HP Pavilion 24-b212d (Z8G27AA#AKL) AIO — macOS High Sierra 10.13.6",
        title_en="HP Pavilion 24-b212d (Z8G27AA#AKL) AIO — macOS High Sierra 10.13.6",
        hw=[
            ("Machine", 'HP Pavilion 24-b212d Z8G27AA#AKL (23.8" All-in-One)'),
            ("CPU", "Intel Core i5-7400T 2.4GHz"),
            ("RAM", "16GB DDR4 2133MHz"),
            ("GPU", "Intel HD Graphics 630 — ใช้งานได้"),
            ("GPU (ตัวที่สอง)", "NVIDIA GeForce 930MX 4GB — ยังไม่สำเร็จ (Not success)"),
            ("Display", '23.8" FHD IPS Touch'),
            ("macOS", "High Sierra 10.13.6"),
        ],
        efi=[("EFI_HP_Pavilion_24-b212d_Z8G27AA_AKL_AIO.zip", "86494c5d8bd03634c5587b45ed3ece5f"),
             ("EFI_OC_Any.zip", "488b78b476ff7b034cf366713e822302")],
        screenshots=["Screen_Audio.png", "Screen_Ethernet.png", "Screen_Hardware.png",
                     "Screen_Hight_Siera_10.13.6.png", "Screen_Intel_Gfx_HD_630.png"],
        notes=[],
        observations=[
            "repo ต้นฉบับบรรจุ EFI สองชุด: ชุดเฉพาะเครื่องนี้ และ `EFI_OC_Any.zip` "
            "(คัดลอกไปไว้ที่ `shared/opencore-any/` แล้ว)",
        ],
    ),
]


LOCAL_ENTRIES = [
    dict(
        vendor="dell-precision-t3420",
        os_slug="macos-sequoia-15.7",
        src="local/dell-precision-t3420-sequoia",
        branch="local",
        origin="local",
        src_path=os.path.join(ROOT, "_recon", "local", "dell-precision-t3420-sequoia"),
        title_th="Dell Precision T3420 (i7-7700 / Intel HD 630) — macOS Sequoia 15.7.9",
        title_en="Dell Precision T3420 (i7-7700 + Intel HD 630 iGPU) — macOS Sequoia 15.7.9",
        hw=[
            ("Machine", "Dell Precision T3420 (i7-7700 + iGPU)"),
            ("CPU", "Intel Core i7-7700"),
            ("GPU", "Intel HD Graphics 630 (iGPU) — เร่งความเร็วได้ 1536 MB, Metal 3"),
            ("SMBIOS", "**MacPro7,1** — ตัวชี้ขาดที่ทำให้สีถูกต้อง (iMac18,3 ทำให้สีเพี้ยน ฟ้า↔ส้ม)"),
            ("boot-args", "`keepsyms=1 debug=0x100 alcid=11 -no_compat_check -wegnoegpu igfxonln=1 espm=boot`"),
            ("OpenCore", "1.0.8"),
            ("Kext", "17 รายการ: Lilu, VirtualSMC(+SMCProcessor/SuperIO/Battery/Light/DellSensors), "
                     "WhateverGreen, AppleALC/AppleALCU (alcid=11), IntelMausi + IntelMausiEthernet, "
                     "USBToolBox/UTBDefault, XHCI-unsupported, AMFIPass, RestrictEvents"),
            ("iGPU properties", "`AAPL,ig-platform-id=00001659` · `device-id=16590000` · "
                                "`framebuffer-patch-enable` · `framebuffer-con1/-con2-type=HDMI` · "
                                "`enable-hdmi-dividers-fix` · `framebuffer-stolenmem=00003001` (≈19 MB)"),
            ("ธีม / Theme", "GoldenGate (`PickerMode=External`, `PickerVariant=Acidanthera\\GoldenGate`)"),
            ("macOS", "Sequoia 15.7.9 (24G830)"),
        ],
        efi=[("EFI-Dell-Precision-3420.zip", "564dc53c43a240fef881c2d548f18f08")],
        screenshots=[],
        notes=["EFI-Dell-Precision-3420.md"],
        observations=[
            "**จุดสำคัญที่แก้สำเร็จ:** สีเพี้ยน (Framebuffer Depth 30-bit) แก้ด้วยการเปลี่ยน SMBIOS "
            "จาก `iMac18,3` เป็น **`MacPro7,1`** และอาการจอค้าง/ดับหลังเข้าหน้าจอ แก้ด้วย boot-arg "
            "**`igfxonln=1`** — ตัวอื่น (เวอร์ชัน OpenCore/Lilu/WhateverGreen, EDID override, "
            "`agdpmod=ignore`, OCLP) ทดสอบแล้ว **ไม่ใช่สาเหตุ**",
            "เอกสารต้นฉบับเรียกเครื่องว่า **Dell OptiPlex** (i7-7700 / Intel HD 630) แต่ชื่อไฟล์ EFI "
            "และโฟลเดอร์ใน zip เป็น **Dell Precision T3420** — ยังไม่ยืนยันว่าเป็นเครื่องเดียวกัน "
            "หรือเขียนชื่อรุ่นผิด จึงเก็บชื่อตามไฟล์ EFI และคงข้อความเดิมไว้ในเอกสาร",
            "ค่าที่สกัดจาก `OC/config.plist` ตรงกับเอกสารทุกจุด (SMBIOS, boot-args, ig-platform-id, stolenmem)",
            "ใน zip มีไฟล์สำรอง `config.plist.bak1..bak22`, `config.plist.presafe-*` และ `_old-kexts/` "
            "ติดมาด้วย — เก็บไว้ตามต้นฉบับ ไม่ได้ตัดออก",
            "เครื่องนี้มี 2 EFI ที่สลับเองได้ → ฝัง marker ใน boot-args (`espm=efi` = EFI หลัก, "
            "`espm=boot` = EFI สำรอง) ชุดนี้เป็น `espm=boot`",
        ],
    ),
    dict(
        vendor="macpro-late-2013",
        os_slug="macos-sequoia-15.x",
        src="local/macpro-late-2013-sequoia",
        branch="local",
        origin="local",
        src_path=os.path.join(ROOT, "_recon", "local", "macpro-late-2013-sequoia"),
        title_th="Apple Mac Pro (Late 2013) — macOS Sequoia 15.x",
        title_en="Apple Mac Pro (Late 2013) — macOS Sequoia 15.x",
        hw=[
            ("Machine", "Apple Mac Pro (Late 2013)"),
            ("SMBIOS", "ไม่กำหนดทับ — `PlatformInfo/Generic` ว่าง (ใช้ค่าเดิมของเครื่องจริง)"),
            ("boot-args", "`keepsyms=1 debug=0x100 -lilubetaall ipc_control_port_options=0 -nokcmismatchpanic`"),
            ("Drivers", "OpenRuntime.efi, OpenCanopy.efi, OpenLinuxBoot.efi, ResetNvramEntry.efi"),
            ("Kext", "15 รายการ: Lilu, RestrictEvents, NVMeFix, AMFIPass, AirportBrcmFixup, "
                     "IOSkywalkFamily, IO80211FamilyLegacy (+AirPortBrcmNIC), CryptexFixup, RSRHelper, "
                     "AppleIntelCPUPowerManagement(+Client), USB-Map, ECM-Override, CatalinaIntelI210Ethernet, "
                     "AutoPkgInstaller"),
            ("ธีม / Theme", "GoldenGate (`PickerMode=External`)"),
            ("macOS", "Sequoia 15.x — อ้างจากชื่อไฟล์ (ไม่ได้ระบุเลขเวอร์ชันย่อย)"),
        ],
        efi=[("EFI-Macpro-Late2013-Sequoia.zip", "705a1846e368b099fd17e5398136b6d2")],
        screenshots=[],
        notes=[],
        observations=[
            "**ไม่มีเอกสารประกอบในชุดที่อัปโหลด** — ข้อมูลในหน้านี้สกัดจาก `OC/config.plist` "
            "และรายการไฟล์ใน zip จริง ไม่ได้คัดลอกจากที่อื่น",
            "ชุดนี้ออกแบบสำหรับ **เครื่อง Mac จริง** (ไม่ตั้ง SMBIOS ทับ) และมีโฟลเดอร์ `APPLE/CACHES` "
            "พร้อม kext สาย legacy (`CryptexFixup`, `RSRHelper`, `AutoPkgInstaller`, "
            "`IO80211FamilyLegacy`) → ลักษณะของชุดที่ทำด้วย **OpenCore Legacy Patcher (OCLP)**",
            "zip ติดไฟล์ metadata ของ macOS (`__MACOSX/`, `._*`, `.DS_Store`) มาด้วย — เก็บตามต้นฉบับ",
            "ไม่พบ `SystemProductName` ใน config จึงยืนยันรุ่นเครื่องจากไฟล์ไม่ได้ "
            "นอกจากชื่อไฟล์ที่ระบุ Mac Pro Late 2013",
        ],
    ),
]


def all_entries():
    return ENTRIES + LOCAL_ENTRIES


def build_readme(e: dict) -> str:
    lines = []
    lines.append("# " + e["title_th"])
    lines.append("")
    lines.append("> " + e["title_en"])
    lines.append("")
    if e.get("origin") == "local":
        lines.append("ที่มา: ไฟล์ที่อัปโหลดโดยเจ้าของ repo (local upload) — "
                     "ข้อมูลสกัดจาก `OC/config.plist` และรายการไฟล์ใน zip จริง")
    else:
        lines.append("ต้นทาง: [`" + e["src"] + "`](https://github.com/" + OWNER + "/" + e["src"] + ") "
                     "(branch `" + e["branch"] + "`)")
    lines.append("")
    lines.append("## ข้อมูลเครื่อง / Hardware")
    lines.append("")
    lines.append("| รายการ | ค่า |")
    lines.append("|---|---|")
    for k, v in e["hw"]:
        lines.append("| " + k + " | " + v + " |")
    lines.append("")
    lines.append("## ไฟล์ EFI")
    lines.append("")
    lines.append("| ไฟล์ | md5 |")
    lines.append("|---|---|")
    for name, _ in e["efi"]:
        fname = norm(name)
        lines.append("| [`" + fname + "`](./" + fname + ") | `" + md5_(os.path.join(REPO, "configs", e["vendor"], e["os_slug"], fname)) + "` |")
    lines.append("")
    if e["screenshots"]:
        lines.append("## ภาพหน้าจอ / Screenshots")
        lines.append("")
        lines.append("<details><summary>คลิกเพื่อดูภาพทั้งหมด ("
                     + str(len(e["screenshots"])) + " ภาพ)</summary>")
        lines.append("")
        for s in e["screenshots"]:
            n = norm(s)
            lines.append("**" + n + "**")
            lines.append("")
            lines.append("![`" + n + "`](./screenshots/" + n + ")")
            lines.append("")
        lines.append("</details>")
        lines.append("")
    if e["notes"]:
        lines.append("## เอกสารต้นฉบับ / Original notes")
        lines.append("")
        for n in e["notes"]:
            lines.append("- [`notes/" + norm(n) + "`](./notes/" + norm(n) + ")")
        lines.append("")
    if e["observations"]:
        lines.append("## ข้อสังเกต / Observations")
        lines.append("")
        for o in e["observations"]:
            lines.append("- " + o)
        lines.append("")
    lines.append("## วิธีใช้ / Usage")
    lines.append("")
    lines.append("1. ดาวน์โหลดไฟล์ EFI zip ในโฟลเดอร์นี้")
    lines.append("2. แตก zip และคัดลอกโฟลเดอร์ `EFI/` ลง EFI System Partition (ESP) ของเครื่อง")
    lines.append("3. ปรับ `config.plist` (SMBIOS / serial) ให้ตรงกับเครื่องของคุณก่อนใช้งาน")
    lines.append("4. ตรวจสอบ md5 ของ zip ให้ตรงกับตารางด้านบนก่อนใช้")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("_ไฟล์นี้สร้างโดย `tools/build.py` — แก้ไขที่ generator ไม่ใช่แก้ไฟล์นี้ตรง ๆ_")
    lines.append("")
    return "\n".join(lines)


def md5_(p: str) -> str:
    return md5(p) if os.path.exists(p) else "?"


def main() -> int:
    if "--list-repos" in sys.argv:
        for e in ENTRIES:
            print(e["src"] + " " + e["branch"])
        return 0

    problems = []

    # 1) ล้างโฟลเดอร์ที่ generate ใหม่ (ไม่แตะ tools/)
    for d in ("configs", "shared", "upstream"):
        shutil.rmtree(os.path.join(REPO, d), ignore_errors=True)

    # 2) คัดลอกไฟล์ + ตรวจ md5 กับ baseline
    for e in all_entries():
        src_dir = e.get("src_path") or os.path.join(UP, e["src"])
        if not os.path.isdir(src_dir):
            problems.append("missing upstream: " + e["src"])
            continue
        dst = os.path.join(REPO, "configs", e["vendor"], e["os_slug"])
        os.makedirs(os.path.join(dst, "screenshots"), exist_ok=True)
        if e["notes"]:
            os.makedirs(os.path.join(dst, "notes"), exist_ok=True)

        # จับคู่ชื่อไฟล์แบบ normalized (ต้นทางบางไฟล์มีช่องว่างในชื่อ)
        actual = {}
        for f in os.listdir(src_dir):
            if os.path.isfile(os.path.join(src_dir, f)):
                actual[norm(f)] = f

        for name, baseline in e["efi"]:
            real = actual.get(norm(name))
            if real is None:
                problems.append("missing source file: " + e["src"] + "/" + name)
                continue
            d = os.path.join(dst, norm(name))
            shutil.copy2(os.path.join(src_dir, real), d)
            got = md5(d)
            if got != baseline:
                problems.append("md5 mismatch after copy: %s (want %s got %s)" % (name, baseline, got))

        for s in e["screenshots"]:
            real = actual.get(norm(s))
            if real is None:
                problems.append("missing screenshot: " + e["src"] + "/" + s)
                continue
            shutil.copy2(os.path.join(src_dir, real),
                         os.path.join(dst, "screenshots", norm(s)))

        for n in e["notes"]:
            real = actual.get(norm(n))
            if real is None:
                problems.append("missing note: " + e["src"] + "/" + n)
                continue
            shutil.copy2(os.path.join(src_dir, real),
                         os.path.join(dst, "notes", norm(n)))

        with open(os.path.join(dst, "README.md"), "w", encoding="utf-8") as f:
            f.write(build_readme(e))

    # 3) upstream/ (สำเนาเอกสารต้นฉบับเพื่อ traceability)
    for e in all_entries():
        src_dir = e.get("src_path") or os.path.join(UP, e["src"])
        if not os.path.isdir(src_dir):
            continue
        dst = os.path.join(REPO, "upstream", e["src"])
        os.makedirs(dst, exist_ok=True)
        for f in sorted(os.listdir(src_dir)):
            if f.lower().endswith((".md", ".txt")) and os.path.isfile(os.path.join(src_dir, f)):
                shutil.copy2(os.path.join(src_dir, f), os.path.join(dst, norm(f)))
        with open(os.path.join(dst, "SOURCE.md"), "w", encoding="utf-8") as f:
            f.write("# แหล่งที่มา / Source\n\n")
            if e.get("origin") == "local":
                f.write("- ที่มา: ไฟล์ที่อัปโหลดโดยเจ้าของ repo (local upload)\n")
            else:
                f.write("- repo: https://github.com/%s/%s\n" % (OWNER, e["src"]))
                f.write("- branch: `%s`\n" % e["branch"])
            f.write("- คัดลอกเมื่อ / copied at: %s\n" % datetime.date.today().isoformat())
            f.write("\nไฟล์ในโฟลเดอร์นี้เป็นสำเนาเอกสารต้นฉบับ (README/txt) ห้ามแก้\n")

    # 4) shared/opencore-any
    sh = os.path.join(REPO, "shared", "opencore-any")
    os.makedirs(sh, exist_ok=True)
    src = os.path.join(UP, "HP-Pavilion-24-b212d-Z8G27AA-AKL-AIO", "EFI_OC_Any.zip")
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(sh, "EFI_OC_Any.zip"))
        if md5(os.path.join(sh, "EFI_OC_Any.zip")) != "488b78b476ff7b034cf366713e822302":
            problems.append("md5 mismatch: shared/opencore-any/EFI_OC_Any.zip")
    else:
        problems.append("missing source: EFI_OC_Any.zip")
    with open(os.path.join(sh, "README.md"), "w", encoding="utf-8") as f:
        f.write("# OpenCore EFI (generic) / EFI OpenCore ทั่วไป\n\n"
                "ชุด EFI OpenCore สำหรับใช้งานทั่วไป (ไม่ผูกกับเครื่องใดเครื่องหนึ่ง)\n"
                "Generic OpenCore EFI bundle — not tied to a specific machine.\n\n"
                "ที่มา / Origin: repo `HP-Pavilion-24-b212d-Z8G27AA-AKL-AIO` ของ sealfx\n")

    # 5) README กลาง + TEMPLATE + repo-meta
    rows = []
    for e in all_entries():
        hwd = dict(e["hw"])
        def g(*keys):
            for k in keys:
                if k in hwd:
                    return hwd[k]
            return "-"
        rows.append("| [%s](configs/%s/%s/README.md) | %s | %s | %s | %s | %s |" % (
            hwd.get("Machine", hwd.get("Workstation", hwd.get("Mainboard / เมนบอร์ด", e["vendor"]))),
            e["vendor"], e["os_slug"],
            g("macOS"),
            g("CPU"),
            g("GPU", "VGA"),
            g("Audio / เสียง", "Audio / Sound", "Audio"),
            g("LAN / เน็ตเวิร์ก", "Ethernet"),
        ))

    root = []
    root.append("# EFI-OSX86")
    root.append("")
    root.append("รวม EFI Hackintosh (x86 / OSX86) ของเครื่องหลายรุ่นไว้ในที่เดียว "
                "แต่ละชุดแยกตาม **เครื่อง × เวอร์ชัน macOS** พร้อม md5 ทุกไฟล์")
    root.append("")
    root.append("A consolidated collection of Hackintosh EFI configurations, organized by "
                "**machine × macOS version**, each with verified md5 checksums.")
    root.append("")
    root.append("## สารบัญ / Index")
    root.append("")
    root.append("| เครื่อง / Machine | macOS | CPU | GPU | Audio | LAN |")
    root.append("|---|---|---|---|---|---|")
    root.extend(rows)
    root.append("")
    root.append("## โครงสร้าง / Layout")
    root.append("")
    root.append("```")
    root.append("EFI-OSX86/")
    root.append("├── configs/<machine>/<macos-version>/   # EFI zip + screenshots + README")
    root.append("├── shared/opencore-any/                  # EFI OpenCore ทั่วไป")
    root.append("├── docs/                                 # ตารางฮาร์ดแวร์ + กติกาการแก้ไข")
    root.append("├── upstream/                             # สำเนาเอกสารต้นฉบับ (traceability)")
    root.append("├── tools/                                # sync / verify / patch")
    root.append("└── MANIFEST.md5                          # md5 ของทุกไฟล์")
    root.append("```")
    root.append("")
    root.append("## ใช้งานเร็ว / Quick start")
    root.append("")
    root.append("```bash")
    root.append("# ตรวจความถูกต้องของทุกไฟล์")
    root.append("bash tools/verify_md5.sh")
    root.append("")
    root.append("# ดึงต้นทางล่าสุดจาก GitHub แล้วสร้างใหม่ (idempotent)")
    root.append("bash tools/sync.sh")
    root.append("```")
    root.append("")
    root.append("## ⚠️ ก่อนใช้งาน / Before you start")
    root.append("")
    root.append("1. **EFI เหล่านี้ผูกกับฮาร์ดแวร์รุ่นนั้น ๆ** — เครื่องต่างรุ่นใช้แทนกันไม่ได้รับประกัน "
                "ต้องปรับ `config.plist` (SMBIOS, device properties) เองก่อนใช้")
    root.append("2. **สร้าง SMBIOS serial ของคุณเองก่อนใช้งาน** (เช่นด้วย GenSMBIOS) — "
                "**อย่าใช้ serial/MLB/UUID ที่ติดมากับไฟล์** เพราะจะซ้ำกับคนอื่นและทำให้ iCloud/iMessage มีปัญหา")
    root.append("3. ตรวจ md5 ของไฟล์ที่ดาวน์โหลดให้ตรงกับ [`MANIFEST.md5`](./MANIFEST.md5) ก่อนใช้ทุกครั้ง")
    root.append("4. สำรอง EFI ที่ใช้อยู่เดิมก่อนเขียนทับ")
    root.append("")
    root.append("## เอกสาร / Documentation")
    root.append("")
    root.append("| เอกสาร | เนื้อหา |")
    root.append("|---|---|")
    root.append("| [`docs/HOW-TO-USE.md`](./docs/HOW-TO-USE.md) | ขั้นตอนใช้งานจริง: mount ESP, สำรอง, คัดลอก EFI, สร้าง serial, reset NVRAM |")
    root.append("| [`docs/HARDWARE-MATRIX.md`](./docs/HARDWARE-MATRIX.md) | ตารางฮาร์ดแวร์ทุกเครื่องในที่เดียว |")
    root.append("| [`docs/CREDITS.md`](./docs/CREDITS.md) | โครงการต้นทาง + kext/เวอร์ชันที่ตรวจพบจริง |")
    root.append("| [`docs/CONTRIBUTING.md`](./docs/CONTRIBUTING.md) | กติกาการแก้ไข (SOP) และวิธีเพิ่มเครื่องใหม่ |")
    root.append("")
    root.append("## หมายเหตุ / Notes")
    root.append("")
    root.append("- ไฟล์ EFI เก็บเป็น zip ต้นฉบับ **ไม่แตกและไม่บีบอัดใหม่** เพื่อรักษาไบต์เดิม")
    root.append("- ทุกไฟล์มี md5 บันทึกใน [`MANIFEST.md5`](./MANIFEST.md5)")
    root.append("- โครงการ/kext ต้นทางดูที่ [`docs/CREDITS.md`](./docs/CREDITS.md)")
    root.append("- EFI เหล่านี้มาจากเครื่องจริงที่เคยใช้งานได้ ณ เวอร์ชัน macOS ที่ระบุ "
                "การนำไปใช้กับเครื่องอื่นต้องปรับ `config.plist` / SMBIOS เอง")
    root.append("")
    with open(os.path.join(REPO, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(root))

    with open(os.path.join(REPO, "repo-meta.json"), "w", encoding="utf-8") as f:
        json.dump({
            "name": "EFI-OSX86",
            "description": "รวม EFI Hackintosh (OSX86) สำหรับ Gigabyte GA-H61M-DS2, Dell Precision T3420/T7450 AIO, HP Pavilion 24-b212d — Catalina 10.15.4 / High Sierra 10.13.6 / Sierra 10.12.x",
            "homepage": "",
            "topics": ["hackintosh", "efi", "opencore", "clover", "osx86", "macos",
                       "catalina", "high-sierra", "sierra", "kexts", "efi-config"],
            "default_branch": "main",
        }, f, ensure_ascii=False, indent=2)
        f.write("\n")

    # 5b) docs/HARDWARE-MATRIX.md
    os.makedirs(os.path.join(REPO, "docs"), exist_ok=True)
    m = []
    m.append("# ตารางฮาร์ดแวร์ / Hardware matrix")
    m.append("")
    m.append("| เครื่อง | macOS | CPU | Chipset | RAM | GPU | Audio | LAN | Storage | Display | EFI |")
    m.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for e in all_entries():
        hwd = dict(e["hw"])

        def gg(*keys):
            for k in keys:
                if k in hwd and hwd[k] not in ("-", ""):
                    return hwd[k]
            return "-"

        m.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | `%s` |" % (
            gg("Machine", "Workstation", "Mainboard / เมนบอร์ด"),
            gg("macOS"), gg("CPU"), gg("Chipset"), gg("RAM"), gg("GPU", "VGA"),
            gg("Audio / เสียง", "Audio / Sound"), gg("LAN / เน็ตเวิร์ก"),
            gg("Storage"), gg("Display"), norm(e["efi"][0][0])))
    m.append("")
    m.append("_สร้างโดย tools/build.py_")
    m.append("")
    with open(os.path.join(REPO, "docs", "HARDWARE-MATRIX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(m))

    # 6) MANIFEST.md5
    files = []
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in filenames:
            if fn == "MANIFEST.md5":
                continue
            p = os.path.join(dirpath, fn)
            files.append((os.path.relpath(p, REPO), p))
    files.sort()
    with open(os.path.join(REPO, "MANIFEST.md5"), "w", encoding="utf-8") as f:
        for rel, p in files:
            f.write("%s  %s\n" % (md5(p), rel))

    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  -", p)
        return 1
    print("OK: built %d files under EFI-OSX86" % (len(files) + 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
