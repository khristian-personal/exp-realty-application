# PROJECT 2: Hardware Deployment & Dual-Boot Configuration Guide

**Objective:** Document your actual hackintosh build as a professional hardware deployment and troubleshooting guide, demonstrating hands-on technical expertise in hardware compatibility, BIOS configuration, and dual-boot environment management.

**Deliverables:**
1. Hardware Specifications & Compatibility Checklist
2. BIOS Configuration Reference
3. Dual-Boot Installation Guide (step-by-step)
4. Thermal Management & Optimization Strategies
5. Troubleshooting Decision Tree
6. KBA: Hardware Deployment Checklist for Remote Teams
7. KBA: Dual-Boot & Multi-OS Environment Management

**Time to Complete:** 3–4 hours  
**Status:** Ready to build (using your actual build as reference)

---

## PART 1: Hardware Specifications & Compatibility Matrix

### Your Build (Complete Specs)

| Component | Specification | Rationale | Driver Status |
|-----------|---------------|-----------|----------------|
| **Case** | Lian Li O11 Vision | Premium airflow, tempered glass, modular | N/A - case only |
| **Motherboard** | MSI MPG X870E Edge Ti WiFi | PCIe 5.0, WiFi 7, DDR5, high-end AM5 socket | Fully supported (X870E drivers available) |
| **CPU** | AMD Ryzen 9950X3D | 16-core/32-thread, Zen 5, high performance | Fully supported |
| **GPU** | NVIDIA RTX 5080 | Latest generation, ray tracing, DLSS 4 | Fully supported (NVIDIA drivers) |
| **RAM** | [Specify: DDR5 MHz, capacity] | [Your specs] | Fully supported |
| **Storage** | [Specify: SSD type, capacity] | [Your specs] | Fully supported |
| **Power Supply** | Lian Li Edge 1000W | Modular, 80+ Platinum, sufficient headroom for RTX 5080 | N/A |
| **CPU Cooling** | Tryx AIO Liquid Cooler | 360mm/420mm, high performance cooling | Fully supported |
| **Case Fans** | Lian Li TL Wireless LCD Fans | Wireless control, RGB, low noise | **KEY CHALLENGE:** Wireless receiver requires special configuration |

### Compatibility Checklist (For New Deployments)

When deploying similar systems, verify:

```
PRE-PURCHASE VERIFICATION
☐ CPU supported by motherboard (socket match: AM5)
☐ RAM compatibility with motherboard (DDR5 support, speed compatible)
☐ GPU has PCI-e slots (X870E has sufficient PCIe lanes)
☐ Storage drives compatible (M.2 NVMe with appropriate speeds)
☐ Power supply wattage sufficient for all components
☐ Case supports motherboard form factor + cooler height
☐ WiFi/Bluetooth chipset driver support verified
☐ All drivers available for Windows and any secondary OS
☐ Wireless peripherals (fans, keyboard, mouse) compatible with OS

PRE-BUILD PHYSICAL
☐ All components visually inspected for damage
☐ Thermal paste (if CPU cooler doesn't include it)
☐ M.2 drive mounting brackets and screws
☐ Power supply modular cables organized
☐ Anti-static wrist strap ready

BUILD ASSEMBLY
☐ CPU installed correctly (no bent pins, proper seating)
☐ RAM seated firmly in slots
☐ M.2 NVMe drives installed
☐ Motherboard mounted with all standoff screws
☐ AIO liquid cooler mounted and thermal paste applied
☐ GPU installed in appropriate PCIe slot
☐ All power connectors secure (24-pin, 8-pin CPU, GPU power)
☐ Case fans mounted and connected
☐ Cables routed cleanly (for airflow)
☐ Power supply connected and switched to ON

PRE-OS INSTALLATION
☐ Power on test (if it doesn't power on, troubleshoot immediately)
☐ BIOS boot screen appears
☐ Monitor displays output
☐ All fans spinning (listen for noise, check visually)
```

---

## PART 2: BIOS Configuration Reference

### Critical BIOS Settings (Step-by-Step for Your Motherboard)

**Access BIOS:**
- Power on computer
- Press **Delete** key repeatedly during boot (before OS loads)
- Enter BIOS setup screen

**Essential Settings for Your Configuration:**

### 1. **CPU Settings**
```
Location: Settings → Advanced → CPU Configuration

Power Performance Tuning:
  ├─ Precision Boost: ENABLED (AMD performance enhancement)
  ├─ Precision Boost Overdrive: ENABLED or AUTO (depends on cooling)
  └─ SMT (Simultaneous Multi-Threading): ENABLED

CPU Clock Ratio: AUTO (let motherboard handle)
CPU VCORE Voltage: AUTO (starts at 1.40V, may adjust under load)
CPU LLC (Load Line Calibration): ENABLED (stabilizes voltage under load)
```

### 2. **Memory Settings** (Critical for DDR5)
```
Location: Settings → Advanced → Memory

DOCP Profile: ENABLED (AMD's equivalent to Intel XMP)
  └─ Select: DOCP Standard (your RAM's rated speed)
  
Memory Speed: Auto-detected after DOCP enabled
Memory Voltage: Auto (typically 1.40V for DDR5)
Primary Timings: Auto (DOCP handles this)

Check after enabling DOCP:
  - Boot successfully?
  - If not: try DOCP Safe setting
  - Still not? → manual timings (requires testing)
```

### 3. **Storage/NVMe Settings**
```
Location: Settings → Advanced → SATA Configuration

M.2 Slot Configuration:
  ├─ M.2_1 (Primary): NVMe PCIe Gen 4/5
  ├─ M.2_2 (Secondary): NVMe PCIe Gen 3
  └─ M.2_3 (Third): NVMe PCIe Gen 3

XMP/DOCP for Storage: N/A (not applicable to NVMe drives)
AHCI Mode: ENABLED (for SATA drives, if used)
```

### 4. **GPU & PCIe Settings**
```
Location: Settings → Advanced → PCI Subsystem

PCIe Slot Configuration:
  ├─ PCIe_1 (GPU): Auto (will run at PCIe 5.0)
  └─ PCIe_3 (WiFi, if applicable): Auto

PCIe Speed: Gen 5 (for modern GPUs)
Above 4G Decoding: ENABLED (allows GPU VRAM above 4GB addressing)
IOPCIE Port Configuration: Auto
```

### 5. **Fan Control & Thermal Settings** (YOUR CRITICAL CHALLENGE)
```
Location: Settings → Advanced → Thermal

Smart Fan Control: ENABLED

Fan Headers Configuration:
  ├─ CPU_FAN (CPU Cooler - AIO): Smart
  ├─ SYSOUTPUT_FAN (Case Fans): Smart
  └─ All headers: Smart or PWM (depending on fan type)

Custom Fan Curve (if needed):
  30°C → 30% speed
  40°C → 40% speed
  50°C → 60% speed
  60°C → 80% speed
  70°C → 100% speed

Temperature Limits:
  ├─ CPU Throttle Temp: 90°C (default)
  ├─ CPU Shutdown Temp: 110°C (emergency)
  └─ HDD Temp Throttle: Disabled (no mechanical drives)

IMPORTANT FOR WIRELESS FANS:
→ See "Wireless Fan Integration" section below
```

### 6. **Wireless & USB Settings** (WIRELESS FAN RECEIVERS)
```
Location: Settings → Advanced → Onboard Devices Configuration

WiFi Adapter: ENABLED (but confirm after OS install)

USB Configuration:
  ├─ USB Legacy Support: Disabled (unless using USB keyboard before OS loads)
  ├─ USB Ports: All enabled
  └─ USB 3.0 Hub: ENABLED

XHCI Handoff: ENABLED (allows Windows to control USB 3.0 natively)

Wireless 2.4GHz/5GHz Bands: ENABLED

CRITICAL FOR YOUR CASE:
If wireless fan receiver won't pair in BIOS:
  → This is expected (receiver is a consumer device, BIOS doesn't control it)
  → Receiver pairs when OS boots (driver loads, USB enumeration)
  → If fans don't appear in software (L-Connect 3), troubleshoot OS-side (see Section 3)
```

### 7. **Boot & Secure Boot Settings** (FOR DUAL-BOOT)
```
Location: Settings → Boot or Security

Secure Boot: Check current setting
  ├─ If Windows only → ENABLED (recommended)
  ├─ If dual-boot → DISABLED (some OS combinations require this)
  ├─ If secondary OS won't boot → DISABLE and try again
  
Boot Mode: UEFI (not Legacy BIOS)
  └─ Verify this is set correctly (most modern boards default to UEFI)

Boot Device Priority:
  1. Windows/Primary OS (if single-boot)
  2. Configured bootloader for dual-boot
  
Fast Boot: Can be ENABLED (reduces POST time)
  └─ Note: May need to disable for troubleshooting

Boot Options:
  ├─ Boot from USB: ENABLED (for OS installation)
  └─ Network Boot: Disabled (not needed for home build)
```

### 8. **Power Management**
```
Location: Settings → Power Management

Sleep State: S3 (traditional sleep, saves power)
  └─ Alternative: S0 + Low Power Idle (newer standard, may not work on all setups)

AC Power Recovery: Power On (computer powers on if AC returns after outage)

Hibernation Support: Can be DISABLED (uses disk space, not needed for home use)
```

### 9. **Monitoring & Monitoring (In-BIOS Thermal/Fan Display)**
```
Location: Main tab (often visible at boot)

Monitor CPU Temperature in real-time
Monitor Fan Speeds
Monitor Voltages
Monitor Chassis Temperature (if sensor available)

These are informational only in BIOS; detailed monitoring happens in OS via:
  → HWInfo64 (free Windows utility)
  → AMD Ryzen Master (if you want to monitor per-core clocks)
  → MSI Center (motherboard's own software)
  → L-Connect 3 (for Lian Li fans)
```

### Key Point: Wireless Receiver Configuration

Your wireless RGB fan receiver is connected to a USB header on your motherboard. Here's what happens:

```
BIOS Stage:
  - BIOS doesn't "know" about wireless receivers (it's a consumer USB device)
  - BIOS only manages motherboard-level devices
  - Receiver sits on USB bus, waiting for OS to enumerate it

OS Boot (Windows):
  1. Windows loads USB drivers
  2. Windows enumerates USB devices
  3. Receiver appears as generic USB device
  4. L-Connect 3 software (when installed) recognizes receiver
  5. Receiver powers up and waits for fan pairing

If receiver doesn't show in BIOS or Windows:
  → Check USB header connection (physical, verify it's seated)
  → Check BIOS USB settings (all USB headers enabled)
  → Boot into Windows, L-Connect 3 should find it
  → If still not found → try different USB header on motherboard
```

---

## PART 3: OS Installation (Step-by-Step)

### Pre-Installation Checklist

```
☐ Created bootable USB drive with OS installer
☐ Motherboard BIOS updated to latest version (check MSI website)
☐ All internal components installed and secured
☐ Power supply switched ON
☐ Monitor, keyboard, mouse connected
☐ Hard drives/NVMe installed in correct slots
☐ Verified in BIOS: all components detected (SSDs visible, RAM recognized)
```

### Windows Installation

**Step 1: Boot from USB**
- Insert bootable Windows USB drive
- Power on computer
- Press **DEL** to enter BIOS (or press **F9** to boot menu on some boards)
- Select USB drive from boot menu
- Press **Enter**

**Step 2: Windows Setup Screen Appears**
- Click "Install Now"
- Accept license terms
- Select "Custom: Install Windows only"

**Step 3: Disk/Partition Selection**
- You'll see your M.2 NVMe drive(s)
- If new drive, it may be "unallocated"
- Select the drive where you want Windows
- Click "Next" (Windows will auto-partition: System Reserved + C: drive)

**Step 4: Installation Begins**
- Computer will restart multiple times (normal)
- Keep USB connected until Windows finishes
- You'll see progress bar (typically 10-20 minutes)

**Step 5: Initial Windows Setup**
- Create user account (use professional name if for work)
- Set password (use strong password manager)
- Configure privacy settings (disable excessive data collection)

**Step 6: Post-Installation**
- Windows Update runs automatically
- Install motherboard chipset drivers (download from MSI website for your model)
- Install GPU drivers (NVIDIA website for RTX 5080)
- Install motherboard management software (MSI Center)
- Install fan control software (L-Connect 3 for Lian Li fans)

### Secondary OS Installation (Example: Dual-Boot Linux)

**Pre-requisite:** Your Windows installation is complete and working

**Step 1: Prepare USB**
- Create bootable Linux USB drive (e.g., Ubuntu 24.04)
- Insert into computer

**Step 2: Resize Windows Partition (Optional)**
- Boot into Windows
- Open Disk Management
- Right-click C: drive → Shrink Volume
- Enter size to shrink (e.g., 200GB if you want 50/50 split)
- Click Shrink
- Windows now has unallocated space for Linux

**Step 3: Boot Linux Installer**
- Power off computer
- Leave Windows USB out, insert Linux USB
- Power on
- Press DEL → enter BIOS
- Set USB as first boot device
- Press F10 to save and exit
- Linux installer boots

**Step 4: Linux Installation**
- Select "Install Ubuntu"
- Choose "Something Else" (custom partitioning)
- Select unallocated space → create new partition
- Choose EXT4 filesystem, mount point /
- Install bootloader to the same disk (where Windows is)
- Continue installation

**Step 5: Bootloader Configuration**
- After Linux install completes, restart
- You should see GRUB menu (Linux bootloader)
- GRUB automatically detected Windows partition
- You can now boot Windows or Linux from GRUB menu

**Important for Dual-Boot:**
- Windows bootloader usually gets overwritten by Linux
- GRUB becomes your bootloader (manages both)
- Both OSes stay isolated on their partitions
- No performance penalty for having both

---

## PART 4: Driver Installation (Correct Order Matters)

### Critical: Driver Load Sequence

Install drivers in this order (chipset first, everything else builds on it):

**Step 1: Motherboard Chipset Drivers** (FIRST - everything depends on this)
1. Go to MSI website
2. Search for your motherboard model: **MSI MPG X870E Edge Ti**
3. Download all chipset drivers
4. Install in this order:
   - AMD Chipset Drivers
   - SATA controller drivers (if using SATA drives)
   - USB 3.0 drivers
   - Audio drivers
5. **RESTART** computer

**Step 2: Network Drivers** (Next priority - you need internet for updates)
6. Download Ethernet/WiFi drivers from MSI website
7. Install network drivers
8. Verify internet connection (critical for next steps)

**Step 3: Storage Drivers** (NVMe performance)
9. M.2 NVMe drivers (usually included in chipset, but verify)
10. AHCI drivers (if using SATA)
11. Restart if prompted

**Step 4: GPU Drivers** (NVIDIA RTX 5080)
12. Go to NVIDIA website → Driver download
13. Select: RTX 5080 → Windows/Linux → Latest driver
14. Download and install (large download, ~500MB)
15. Restart computer
16. Verify in Device Manager (should show "NVIDIA RTX 5080" with no errors)

**Step 5: Motherboard Management Software**
17. Download MSI Center from MSI website
18. Install MSI Center (manage fans, monitoring, etc.)
19. Download MSI Dragon Center (additional OC tools, optional)
20. Restart if prompted

**Step 6: Wireless/Peripheral Software**
21. Install L-Connect 3 (for Lian Li fans)
22. Install AIO monitoring software (for Tryx AIO)
23. Run software, allow it to detect fan receiver and cooler

**Step 7: System Updates**
24. Windows Update → Check for updates
25. Install all critical/security updates
26. Restart multiple times until no more updates
27. Verify GPU drivers didn't get overwritten (GPU settings in Windows)

**Step 8: Verification**
28. Device Manager → Verify no "Unknown devices" or devices with errors
29. Run HWInfo64 (download free from website) → verify all components detected
30. Test cooling (run stress test, verify fans respond)

---

## PART 5: Thermal Management & Fan Configuration

### Your Cooling Setup

- **CPU Cooler:** Tryx AIO (2x/3x 120mm radiator, pump with LCD screen)
- **Case Fans:** Lian Li TL Wireless LCD fans (3x case fans, wireless controlled)
- **Case Airflow:** Front intake (2-3 fans), top/rear exhaust (1-2 fans)

### Temperature Targets (High-End Build)

```
During Idle/Light Load:
  CPU: 30-45°C
  GPU: 30-40°C
  Motherboard: 30-50°C
  Case ambient: 20-30°C

During Gaming/Load:
  CPU: 60-75°C (target max ~80°C)
  GPU: 75-85°C (NVIDIA limit)
  Motherboard: 50-65°C

Emergency Shutdown:
  CPU: > 110°C (motherboard auto-stops)
  GPU: > 95°C (driver throttles)
```

### Fan Curve Setup (In BIOS or MSI Center)

**Option A: Auto/Smart Fan Curve (Easiest)**
- BIOS: Thermal → Smart Fan Control: Enabled
- Motherboard automatically adjusts fan speed based on temps
- No tuning needed
- Works for most users

**Option B: Custom Fan Curve (For enthusiasts)**

Create this in BIOS or MSI Center:
```
Temp → Fan Speed (PWM%)
30°C → 30%
40°C → 40%
50°C → 50%
60°C → 70%
70°C → 85%
80°C → 95%
90°C → 100%
```

Results in:
- Quieter at low temps (fans ramp up gradually)
- Maximum cooling when needed
- Can be tuned by ear/preference

### Wireless Fan Control (L-Connect 3)

Once L-Connect 3 software is installed and fans are paired:

```
L-Connect 3 Interface:
├─ Fan Control
│  ├─ Auto Mode (motherboard BIOS controls)
│  ├─ Manual Mode (slider control, 0-100%)
│  └─ Custom Profiles (create presets for different scenarios)
│
├─ RGB Control
│  ├─ Color picker (choose fan LED color)
│  ├─ Animation (rainbow, breathing, static, etc.)
│  └─ Brightness
│
└─ Monitoring
   ├─ Real-time RPM for each fan
   ├─ Temperature sensors
   └─ System health status
```

### Thermal Paste Application (Critical!)

If reseating CPU cooler:

```
1. Power off and unplug computer
2. Remove cooler from CPU carefully (twist, don't pull straight)
3. Old thermal paste on CPU IHS (integrated heat spreader):
   - Use alcohol wipes to clean old paste completely
   - Wipe until surface is shiny clean
4. New thermal paste application:
   - Pea-sized amount in center of CPU
   - NOT a line (old myth)
   - NOT covering entire surface (wasted paste, worse performance)
   - Just enough to cover contact when cooler presses down
5. Remount cooler
   - Push down gently with even pressure
   - Tighten screws in diagonal pattern (like car wheel lugs)
   - Don't overtighten (breaks CPU, voids warranty)
6. Power on and verify temps drop to normal range

Important: Too much paste can:
  - Reduce contact
  - Create poor thermal transfer
  - Cause temps to spike
  
Solution: If temps high after paste application, remove cooler and re-apply with less paste.
```

---

## PART 6: Troubleshooting Decision Tree

Use this flowchart when things go wrong:

```
PROBLEM: Computer won't power on
├─ Check: Is power supply switch ON? (back of PSU)
│  └─ If OFF → flip switch, power on
├─ Check: Is 24-pin power connector fully seated?
│  └─ If loose → reseat (press until click)
├─ Check: Is CPU 8-pin power connected?
│  └─ If loose → reseat
├─ Check: Is power cable connected to outlet?
│  └─ If not → connect to different outlet
└─ If still not powering on:
   → Likely PSU failure or motherboard issue
   → Escalate to vendor

PROBLEM: Computer powers on but no display output
├─ Check: Monitor is on and connected?
│  └─ Try different display cable
├─ Check: Is GPU properly seated in PCIe slot?
│  └─ Power off, reseat GPU by pushing firmly
├─ Check: Did GPU drivers install?
│  └─ Boot into Safe Mode → Device Manager → check for GPU driver errors
├─ Check: Is monitor plugged into GPU (not motherboard)?
│  └─ Motherboard has integrated graphics, may default to that
└─ If still no display:
   → Try with only CPU graphics (no GPU) → if works, GPU issue
   → Try with one RAM stick at a time → may be RAM issue

PROBLEM: Computer boots but fans spinning loudly
├─ Check: Thermal paste properly applied?
│  └─ Check temps in HWInfo → if CPU > 80°C under load, likely paste issue
├─ Check: Fan curve tuned too aggressively?
│  └─ BIOS → Thermal → adjust fan curve to less aggressive
├─ Check: Case fans installed correctly for airflow?
│  └─ Front intake, top/rear exhaust (heat should flow out)
└─ Solution:
   → If temps high: reapply thermal paste (see Part 5)
   → If temps normal but fans loud: adjust fan curve

PROBLEM: Wireless fans won't pair/show in L-Connect 3
├─ Check: Is receiver plugged into USB header on motherboard?
│  └─ Reseat USB header connection
├─ Check: Did L-Connect 3 software install fully?
│  └─ Uninstall, restart, reinstall
├─ Check: USB header is enabled in BIOS?
│  └─ BIOS → Advanced → USB Configuration → All headers enabled
├─ Check: Windows recognized the receiver as USB device?
│  └─ Device Manager → Other Devices → any "Unknown" devices?
└─ If still not working:
   → Try different USB header on motherboard
   → Check L-Connect 3 version (update if outdated)
   → Restart computer multiple times

PROBLEM: One of three fans not spinning
├─ Check: Fan header connection on motherboard?
│  └─ Reseat the connector firmly
├─ Check: Is fan actually broken (won't spin manually)?
│  └─ If won't spin even by hand, fan is dead → RMA
├─ Check: Is BIOS controlling that header?
│  └─ BIOS → Thermal → check fan settings for that header
└─ If fan spins manually but not under power:
   → Fan header broken → try different header
   → Restart BIOS settings

PROBLEM: System overheating during load (> 85°C CPU)
├─ Check: Thermal paste properly applied?
│  └─ If unsure, reseat cooler and reapply (see Part 5)
├─ Check: AIO pump running?
│  └─ Listen for pump noise (should hear soft humming)
│  └─ MSI Center → Pump status should show RPM
├─ Check: AIO radiator fans spinning?
│  └─ Verify visually, check BIOS fan header readings
├─ Check: Case airflow set up correctly?
│  └─ Front intake, rear/top exhaust (not reversed)
└─ If still overheating:
   → AIO may have failed (pump dead, no fluid flow)
   → Consider new cooler or better ventilation
```

---

## PART 7: Portfolio Framing

When presenting this project, emphasize:

**Technical Depth:**
> "Documented complete hardware build with advanced configuration including multi-OS support, wireless peripheral integration, and thermal optimization. Demonstrates deep understanding of motherboard architecture, BIOS configuration, driver sequencing, and hands-on troubleshooting across system layers."

**Practical Value:**
> "This guide can be reused for deploying similar systems to users or troubleshooting hardware issues in production. Includes decision trees, step-by-step procedures, and reference tables that enable rapid diagnosis and resolution."

**Your Unique Value:**
> "The wireless RGB fan integration challenge demonstrates persistence in solving edge-case hardware compatibility problems — exactly what help desk support requires when users encounter issues that don't have obvious solutions."

---

## How to Present This in Your Portfolio

Create a folder in your project area:
```
PROJECT_2_HARDWARE_DEPLOYMENT/
├─ Hardware_Specs_Compatibility_Matrix.csv
├─ BIOS_Configuration_Reference.md
├─ OS_Installation_Guide.md
├─ Driver_Installation_Order.txt
├─ Thermal_Management_Guide.md
├─ Troubleshooting_Decision_Tree.md
├─ L-Connect3_Wireless_Fan_Setup.md
└─ README.md (intro explaining the project)
```

**README content:**
```
# Hardware Deployment & Configuration Guide

## Overview
Comprehensive documentation of a high-performance PC build (Lian Li O11, 
RTX 5080, Ryzen 9950X3D) including full BIOS configuration, dual-OS 
installation procedures, driver sequencing, and thermal optimization.

## What This Demonstrates
- Deep understanding of hardware compatibility and system architecture
- Hands-on troubleshooting of complex configuration challenges
- Ability to document technical procedures clearly
- Problem-solving when standard solutions don't apply (wireless fan integration)
- Knowledge applicable to enterprise hardware deployment scenarios

## Files in This Guide
1. Hardware specs and compatibility matrix
2. BIOS reference with critical settings
3. Step-by-step OS installation procedures
4. Driver installation in correct sequence
5. Thermal management and fan curves
6. Decision tree for common hardware issues

## Real-World Application
This approach is directly transferable to:
- New employee hardware provisioning at eXp
- Troubleshooting hardware issues in production
- Creating standardized deployment procedures
- Training other support staff
```

---

## Time Estimate

- Document current build specs: 30 min
- Write BIOS configuration guide: 45 min
- Write OS installation guide: 45 min
- Create driver installation guide: 15 min
- Create troubleshooting decision tree: 30 min
- Write thermal management guide: 30 min
- **Total: ~3.5 hours**

This is your technical showcase project. It's meaty, detailed, and demonstrates real expertise.
