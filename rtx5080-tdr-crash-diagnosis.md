# Case Study: RTX 5080 TDR Crash Diagnosis
**Date:** June 16, 2026  
**System:** Custom PC — AMD 9950X3D, RTX 5080, 1000W Lian Li Gold Edge PSU  
**OS:** Windows 11  
**Game:** Marvel Rivals (Unreal Engine 5, Win64 Shipping build)

---

## Initial Symptoms

- Repeated game crashes during or after high-intensity gameplay
- Lag spikes specifically during transitions from heavy combat to menus/loading screens
- Grey flashes on dual monitor setup, worsening under GPU load — only resolvable by disabling second monitor
- System hard hang requiring manual power reset
- Audio stuttering prior to full system freeze
- Crash during NVIDIA driver installation

---

## Initial Hypothesis

**Thermal throttling + power delivery stress** causing GPU device removal during load transitions.

Supported by:
- `DXGI_ERROR_DEVICE_REMOVED` in UE crash log
- Lag spikes on scene transitions (GPU load dropping suddenly after sustained peak)
- History of fried PSU power cable

---

## System Context

| Component | Detail |
|-----------|--------|
| GPU | RTX 5080 (purchased November 2025) |
| CPU | AMD Ryzen 9 9950X3D |
| PSU | Lian Li Gold Edge 1000W (recently replaced) |
| Monitors | Dual monitor setup (DisplayPort) |
| Lighting/Monitoring | L-Connect Service (Lian Li) |

---

## Diagnostic Process

### Step 1 — UE Crash Log Analysis
**Finding:** `DXGI_ERROR_DEVICE_REMOVED` at `D3D12Submission.cpp Line 843`

D3D12 command execution failed. GPU lost communication with the driver mid-command. 7 residency objects totaling 224MB loaded — normal gameplay load, not a VRAM spike.

**Conclusion:** GPU dropped off the PCIe bus during active rendering. Not a VRAM ceiling issue.

---

### Step 2 — Windows Event Viewer Analysis
**Finding:** `nvlddmkm Event ID 153` — TDR events

First crash log sequence:
```
11:12:58 PM — Restarting TDR occurred on GPUID:100
11:13:03 PM — L-Connect Service terminated unexpectedly
```

**TDR (Timeout Detection and Recovery):** Windows mechanism that detects when a GPU stops responding and attempts a driver-level reset. Repeated TDR events indicate hardware instability, not software misconfiguration.

**Conclusion:** GPU is not just crashing — it is hanging and requiring forced driver recovery.

---

### Step 3 — PSU and Power Delivery
**History:** Previous PSU had a fried GPU power cable. Entire PSU replaced with Lian Li Gold Edge 1000W.

**Power budget check:**
- RTX 5080 TDP: ~320W
- AMD 9950X3D TDP: ~162W
- Total estimated load: ~480W — well within 1000W capacity

**Conclusion:** PSU ruled out as active cause. However, the original fried cable event may have delivered a voltage spike to the GPU during failure.

---

### Step 4 — VRAM Integrity Test
**Tool:** OCCT — GPU VRAM Test  
**Duration:** 30 minutes  
**Result:** No errors detected

**Conclusion:** VRAM cells are intact. Failure is not VRAM corruption. Points toward GPU power delivery circuit or PCIe communication layer.

---

### Step 5 — Dual Monitor Isolation
**Observation:** Grey flashes began the same day a second monitor was connected — predating the PSU failure.

**Hypothesis A:** Dual monitor VRAM bandwidth saturation causing display artifacts and instability.

**Test:** Routed second monitor through motherboard iGPU (AMD integrated graphics on 9950X3D), leaving RTX 5080 driving a single display. Enabled iGPU in BIOS with fixed memory allocation.

**Initial result:** Hard system hang during test — full freeze, audio cut, required manual power reset.

**Revised finding:** Dynamic iGPU memory allocation was competing with game for memory controller bandwidth, causing PCIe bus contention. Switched to fixed iGPU allocation and retested.

**Second result:** First game ran clean. Crashed on second game.

**Conclusion:** Dual monitor bandwidth hypothesis partially ruled out. Crash persists on single GPU display. Grey flash timing with second monitor was likely coincidental — GPU was already degraded from PSU event, dual monitor load simply exposed it earlier.

---

### Step 6 — Second UE Crash Log
**Finding:** `GPU Crash dump Triggered`

Distinct from first crash. This is the GPU's own internal crash reporter — not just a D3D12 command failure, but the GPU itself reporting a fault.

**Conclusion:** Hardware-level fault confirmed.

---

### Step 7 — Detailed TDR Sequence Analysis
Second crash Event Viewer logs:

```
1:11:31 AM — nvlddmkm 153 — "Resetting TDR occurred on GPUID:100"
1:11:34 AM — nvlddmkm 153 — "Reset TDR occurred on GPUID:100"
1:11:37 AM — Service Control Manager 7034 — L-Connect Service terminated
```

**Three-second TDR sequence:**
1. GPU stops responding → driver initiates recovery
2. Driver recovery completes → GPU technically resets
3. System destabilizes from the event → L-Connect crashes as collateral

**Binary payload analysis:**
```
00000000020030000000000099000000...
```
`0x99` = NVIDIA internal hardware fault code. Not a driver error. Not a software error. Hardware.

**Device path:** `\Device\Video3` — GPU enumerated as 4th display adapter alongside iGPU, consistent with test configuration.

**Conclusion:** TDR sequence is textbook GPU hardware failure. Recovery succeeds at driver level but game cannot continue because GPU already dropped commands.

---

### Step 8 — L-Connect Software Interference
**Hypothesis:** L-Connect monitoring suite polls GPU temperature and load data to sync lighting effects. Repeated driver calls during GPU instability could trigger TDR events.

**Test:** 
- Closed L-Connect application fully
- Disabled from Windows startup
- Stopped and disabled all associated Windows services

**Result:** TDR events and crashes persisted identically.

**Conclusion:** L-Connect ruled out as cause. Confirmed downstream victim of GPU instability, not contributor.

---

## Variables Eliminated

| Variable | Test | Result |
|----------|------|--------|
| PSU power delivery | Replaced with 1000W unit | Ruled out |
| VRAM corruption | OCCT 30-min VRAM test | Ruled out |
| Dual monitor bandwidth | Single monitor via iGPU test | Ruled out |
| Dynamic RAM allocation | Fixed iGPU BIOS allocation | Ruled out |
| L-Connect interference | Fully disabled all services | Ruled out |
| DisplayPort cable | Cable swap | Ruled out |
| Thermal throttling | HWiNFO monitoring | No abnormal temps observed |

---

## Root Cause

**RTX 5080 hardware failure** — likely GPU power delivery circuit or internal PCIe communication layer damaged during original PSU cable failure event (voltage spike).

Supporting evidence:
- `GPU Crash dump Triggered` (GPU self-reported fault)
- `nvlddmkm Event ID 153` TDR events with `0x99` hardware fault code
- Crashes persist across all software variable eliminations
- Grey flashes on dual monitor (PCIe signal integrity issue)
- Crash during driver installation (GPU memory test failure)
- OCCT VRAM test passed (rules out cell-level VRAM damage, points to power/PCIe layer)

---

## Resolution

**RMA via Microcenter protection plan.**

GPU purchased November 2025 — within warranty. Presented Event Viewer logs and UE crash dumps as supporting documentation.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Windows Event Viewer | TDR event capture and sequence analysis |
| OCCT | GPU VRAM integrity stress test |
| HWiNFO64 | Real-time GPU temperature and power monitoring |
| Unreal Engine Crash Reporter | Initial crash identification |

---

## Key Takeaways

- `DXGI_ERROR_DEVICE_REMOVED` is a starting point, not a conclusion — always pull Event Viewer logs for the full picture
- TDR events (`nvlddmkm 153`) are the definitive indicator of GPU hardware vs software failure
- `0x99` in the binary payload = NVIDIA hardware fault code
- L-Connect and similar RGB/monitoring software can trigger TDR on marginal hardware — always isolate before RMA
- OCCT VRAM test passing does not rule out GPU failure — power delivery and PCIe layers are separate failure modes
- Voltage events from PSU failures can cause latent GPU damage that only manifests under sustained load

---

*Documented as part of IT portfolio — real-world hardware diagnostic case study.*
