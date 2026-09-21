# เครดิตและที่มา / Credits & third-party components

EFI ใน repo นี้ **ประกอบขึ้นจากโครงการโอเพนซอร์สของชุมชน Hackintosh** ตัว repo นี้มีไว้รวบรวม/จัดระเบียบและบันทึกค่าที่ใช้งานได้จริงเท่านั้น สิทธิ์ในแต่ละส่วนเป็นของผู้พัฒนาเดิม

## โครงการหลัก / Core projects

| โครงการ | หน้าที่ | ที่มา |
|---|---|---|
| OpenCorePkg | bootloader (`OpenCore.efi`, `BOOTx64.efi`, drivers) | github.com/acidanthera/OpenCorePkg |
| OpenCore Legacy Patcher (OCLP) | ชุด kext/patch สำหรับเครื่อง Mac จริงและ iGPU รุ่นเก่า | github.com/dortania/OpenCore-Legacy-Patcher |
| USBToolBox | สร้าง USB map (`USB-Map`, `UTBDefault`) | github.com/USBToolBox/tool |

## kext ที่ตรวจพบใน zip (พร้อมเวอร์ชัน) / Detected kexts

สแกนจาก `Info.plist` ในทุก zip ของ repo นี้ (ข้อมูลจริง ณ วันสร้างไฟล์)

| kext | เวอร์ชันที่พบ | อยู่ในชุด |
|---|---|---|
| `AMFIPass.kext` | 1.4.1 | dell-precision-t3420, macpro-late-2013 |
| `AirportBrcmFixup.kext` | 2.0.7, 2.1.9 | hp-pavilion-24-b212d, macpro-late-2013, shared/opencore-any |
| `AppleALC.kext` | 1.5.1, 1.9.7 | dell-precision-t3420, hp-pavilion-24-b212d, shared/opencore-any |
| `AppleALCU.kext` | 1.9.7 | dell-precision-t3420 |
| `AppleIntelCPUPowerManagement.kext` | 222.0.0 | macpro-late-2013 |
| `AppleIntelCPUPowerManagementClient.kext` | 222.0.0 | macpro-late-2013 |
| `AtherosE2200Ethernet.kext` | 2.1.0d1 | hp-pavilion-24-b212d, shared/opencore-any |
| `AutoPkgInstaller.kext` | 1.0.4 | macpro-late-2013 |
| `CatalinaIntelI210Ethernet.kext` | 2.3.1 | macpro-late-2013 |
| `CryptexFixup.kext` | 1.0.4 | macpro-late-2013 |
| `ECM-Override.kext` | 9.9.9 | macpro-late-2013 |
| `EFICheckDisabler.kext` | 0.5 | hp-pavilion-24-b212d, shared/opencore-any |
| `IO80211FamilyLegacy.kext` | 12.0, 14.0 | macpro-late-2013 |
| `IOSkywalkFamily.kext` | 1.0 | macpro-late-2013 |
| `IntelMausi.kext` | 1.0.3, 1.0.8 | dell-precision-t3420, hp-pavilion-24-b212d, shared/opencore-any |
| `IntelMausiEthernet.kext` | 3.0.3 | dell-precision-t3420 |
| `Lilu.kext` | 1.4.6, 1.7.0, 1.7.2 | dell-precision-t3420, hp-pavilion-24-b212d, macpro-late-2013, shared/opencore-any |
| `LucyRTL8125Ethernet.kext` | 1.0.0d6 | hp-pavilion-24-b212d, shared/opencore-any |
| `NVMeFix.kext` | 1.0.2, 1.1.2 | hp-pavilion-24-b212d, macpro-late-2013, shared/opencore-any |
| `RSRHelper.kext` | 1.0.2 | macpro-late-2013 |
| `RT2870USBWirelessDriver.kext` | 1.3.0.0 | hp-pavilion-24-b212d, shared/opencore-any |
| `RealtekRTL8111.kext` | 2.3.0d10 | hp-pavilion-24-b212d, shared/opencore-any |
| `RestrictEvents.kext` | 1.1.5, 1.1.7 | dell-precision-t3420, macpro-late-2013 |
| `SATA-unsupported.kext` | 0.9.2 | hp-pavilion-24-b212d, shared/opencore-any |
| `SMCBatteryManager.kext` | 1.3.7 | dell-precision-t3420 |
| `SMCDellSensors.kext` | 1.3.7 | dell-precision-t3420 |
| `SMCLightSensor.kext` | 1.3.7 | dell-precision-t3420 |
| `SMCProcessor.kext` | 1.3.7 | dell-precision-t3420 |
| `SMCSuperIO.kext` | 1.3.7 | dell-precision-t3420 |
| `SmallTreeIntel82576.kext` | 1.0 | hp-pavilion-24-b212d, shared/opencore-any |
| `SystemProfilerMemoryFixup.kext` | 1.0.0 | hp-pavilion-24-b212d, shared/opencore-any |
| `USB-Map.kext` | 1.0 | macpro-late-2013 |
| `USBInjectAll.kext` | 0.7.1 | hp-pavilion-24-b212d, shared/opencore-any |
| `USBToolBox.kext` | 1.2.0 | dell-precision-t3420 |
| `UTBDefault.kext` | 1.0 | dell-precision-t3420 |
| `VirtualSMC.kext` | 1.0, 1.1.5, 1.3.7 | dell-precision-t3420, hp-pavilion-24-b212d, shared/opencore-any |
| `WhateverGreen.kext` | 1.4.1, 1.7.0 | dell-precision-t3420, hp-pavilion-24-b212d, shared/opencore-any |
| `XHCI-unsupported.kext` | 0.9.2 | dell-precision-t3420, hp-pavilion-24-b212d, shared/opencore-any |

> สิทธิ์/สัญญาอนุญาตของแต่ละ kext เป็นไปตามโครงการต้นทาง ตรวจสอบได้จากไฟล์ `Info.plist` / `LICENSE` ภายใน kext นั้น ๆ
