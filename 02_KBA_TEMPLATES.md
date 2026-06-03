# Knowledge Base Articles - Templates & Planning

## KBA #1: Hardware Deployment Checklist for Remote Teams

**Target:** 800–1000 words  
**Audience:** IT Managers, Onboarding Staff, New Hire Coordinators  
**Purpose:** Provide a repeatable, documented process for provisioning hardware to remote employees  
**What it demonstrates:** Process documentation, end-to-end thinking, attention to detail, customer service mindset

### Outline

1. **Introduction**
   - Why this checklist matters (remote employees depend entirely on IT)
   - 3-stage process: Pre-Delivery, Arrival & Setup, Post-Arrival Validation

2. **Pre-Delivery (1–2 weeks before hire start date)**
   - Create hardware order (laptop model, peripherals, specs)
   - Configure OS before shipment (user accounts, VPN, essential software)
   - Ship tracking & delivery confirmation
   - Prepare welcome packet (password reset instructions, support contact)
   - Update asset database

3. **Day of Arrival**
   - Confirm delivery receipt
   - First contact call with new hire (30 min support session)
   - Walk through unboxing and setup
   - Install essential software (VPN, antivirus, collaboration tools)
   - Verify network connectivity and VPN access
   - Test email and cloud storage access
   - Screenshot system info for support records

4. **Post-Setup (Week 1)**
   - Security training (password policies, phishing awareness)
   - System access validation (all required applications working)
   - Ongoing support contact options
   - Feedback survey (how was the setup experience?)
   - Documentation in knowledge base

5. **Template Checklist** (printable/copiable form)

6. **Common Issues & Troubleshooting**
   - Slow network during initial sync
   - Driver issues on arrival
   - VPN connection problems
   - Email authentication

7. **Key Metrics to Track**
   - Time to full productivity (target: 2 hours)
   - New hire satisfaction with IT setup
   - Number of follow-up support requests
   - Hardware delivery vs. start date accuracy

---

## KBA #2: Help Desk Ticket Management Best Practices

**Target:** 1000–1200 words  
**Audience:** IT Support Team, Help Desk Analysts, Team Leads  
**Purpose:** Define standardized ticket lifecycle and triage methodology  
**What it demonstrates:** Process thinking, communication skills, operational excellence

### Outline

1. **The Ticket Lifecycle** (visual flowchart)
   - Submission → Triage → Assignment → Resolution → Closure

2. **Ticket Intake & Categorization**
   - Hardware (broken device, peripherals, drivers)
   - Software (installation, licensing, bugs)
   - Account (password, access, new user)
   - Network (connectivity, VPN, speed)
   - Other (escalate to vendor support)
   - **Table: Categories, Examples, Primary Owner**

3. **Priority Levels & SLAs**
   - P1 (Critical): Network down, no email, loss of access — 15 min response
   - P2 (High): Productivity blocked, multiple users affected — 1 hour response
   - P3 (Medium): Workaround available, isolated user — 4 hour response
   - P4 (Low): Enhancement request, minor bug, non-urgent — 24 hour response
   - **Decision tree: How to assign priority**

4. **First-Contact Resolution (FCR) Techniques**
   - Clarifying questions: what changed, what have you tried, when did it start?
   - Quick wins: restart, clear cache, reinstall driver, reset password
   - Documentation: link to relevant KBA before escalating
   - Customer communication: "here's what I found, here's what we'll do next"

5. **Escalation Criteria**
   - Hardware failure requiring RMA
   - Vendor software bugs
   - Complex multi-system issues
   - Security incidents or compliance violations
   - Issues outside IT scope (facilities, HR, payroll)
   - **Escalation email template**

6. **Ticket Documentation Standards**
   - Initial summary (one sentence: what's the issue?)
   - Steps taken to diagnose
   - Solution implemented
   - Time spent
   - Link to relevant KBA or ticket history
   - Follow-up needed? (yes/no, explain)

7. **Customer Communication Templates**
   - Initial acknowledgment (within 15 min)
   - Status update (if resolution > 30 min)
   - Resolution notification with next steps
   - Closure survey (satisfaction, likelihood to recommend)

8. **SLA Tracking & Metrics**
   - Average response time (target: under 30 min)
   - Average resolution time (target: under 4 hours)
   - First-contact resolution rate (target: 60%+)
   - Customer satisfaction score (target: 4.5/5)
   - Ticket volume trend (month over month)

---

## KBA #3: Dual-Boot & Multi-OS Environment Management

**Target:** 1000–1400 words  
**Audience:** IT Technicians, Hardware Engineers, Advanced Users  
**Purpose:** Comprehensive guide to setting up, troubleshooting, and maintaining dual-boot systems  
**What it demonstrates:** Deep technical knowledge, attention to detail, thoroughness, ability to handle complexity

### Outline

1. **Why Dual-Boot Matters**
   - Business use cases (Mac users who need Windows apps, Windows admins who need Mac)
   - Personal productivity (different OS optimized for different workflows)
   - Development environments (cross-platform testing)
   - Risks and considerations

2. **Pre-Install Checklist**
   - Backup existing data
   - Verify hardware compatibility (CPU, RAM, disk space)
   - BIOS/UEFI settings required
   - Disk partitioning strategy (space allocation, partition scheme)
   - Installation media preparation (USB drives, ISO files)

3. **Step-by-Step Installation Process**
   - BIOS/UEFI access and configuration
   - Boot order settings
   - Primary OS installation (with detailed screenshots)
   - Disk partitioning during install
   - Secondary OS installation (with detailed screenshots)
   - Boot loader configuration (managing which OS launches first)

4. **BIOS/Firmware Configuration**
   - Secure Boot (enabled/disabled for each OS)
   - TPM 2.0 settings
   - XMP/DOCP profile enabling (for performance)
   - Temperature & fan curve optimization
   - **Table: BIOS settings for Windows vs. Mac OS**

5. **Driver Installation & Compatibility**
   - Chipset drivers first
   - NIC drivers for network access
   - Storage controllers
   - Audio drivers
   - GPU drivers
   - Platform-specific drivers (Windows: Intel/AMD management tools; Mac: Apple software)

6. **Wireless Peripheral Integration** (advanced section)
   - RGB fans and wireless receivers
   - Pairing protocol and software (L-Connect 3, iCUE, etc.)
   - BIOS constraints and workarounds
   - Driver load order
   - Troubleshooting unpaired devices

7. **Bootloader Management**
   - Understanding EFI and boot manager
   - Rebooting to BIOS vs. OS selection menu
   - Recovery partitions and their role
   - Fixing broken bootloader (step-by-step)

8. **Thermal Management & Monitoring**
   - Thermal compound application
   - Fan curve optimization for each OS
   - Monitoring tools (HWInfo, Corsair Link, Apple Diagnostics)
   - Temperature targets by component
   - Undervolting and power management (if applicable)

9. **Common Issues & Troubleshooting**
   - Won't boot to secondary OS
   - Excessive thermal output (solution: fan curve tuning)
   - Wireless peripherals disconnect randomly
   - Storage allocation errors
   - **Decision tree for common symptoms**

10. **Maintenance & Updates**
    - OS patching strategy (when to update, testing before rolling out)
    - BIOS updates (before or after OS updates?)
    - Driver updates (per-OS strategy)
    - Disk cleanup and defragmentation
    - Regular health checks

11. **Backup & Recovery Strategy**
    - Disk image backups for each OS
    - Recovery partition maintenance
    - Testing restore process
    - Off-site backup location

---

## KBA #4: Troubleshooting Remote Connectivity Issues

**Target:** 900–1100 words  
**Audience:** IT Support, Field Technicians, End Users  
**Purpose:** Structured diagnostic approach to connectivity problems  
**What it demonstrates:** Systematic thinking, troubleshooting methodology, clear customer communication

### Outline

1. **The OSI Model & Where Issues Hide**
   - Physical layer (cables, wireless signal)
   - Data link layer (MAC addresses, switches)
   - Network layer (IP, routing)
   - Transport layer (TCP/UDP, ports)
   - Application layer (DNS, VPN)

2. **First Contact Triage Questions**
   - "Can you see any network at all?" → Physical connection
   - "Can you see the network but not connect?" → Authentication
   - "Can you connect but not reach the internet?" → Routing
   - "Can you reach the internet but not your apps?" → DNS or firewall
   - "Everything works but it's slow?" → Bandwidth or congestion

3. **Quick Diagnostic Flowchart**
   - Is WiFi enabled? → Restart router
   - Is Ethernet plugged in? → Check physical cable
   - Can you see the network? → Is it yours?
   - Can you connect? → Is authentication correct?
   - Can you reach gateway? → ping 8.8.8.8
   - Can you reach internet? → Check DNS, test nslookup
   - Can you reach VPN? → Check certificate, tunnel status

4. **Windows-Specific Diagnostics**
   - `ipconfig /all` (show current IP config)
   - `ping` (test connectivity)
   - `nslookup` (test DNS resolution)
   - `tracert` (trace route to destination)
   - `netsh int reset` (nuclear option to reset stack)
   - Network troubleshooter (built-in GUI tool)

5. **Mac-Specific Diagnostics**
   - System Preferences → Network
   - `ifconfig` (show network config)
   - `ping` and `nslookup` (same as Windows)
   - `networksetup` (macOS command-line tool)
   - Wireless Diagnostics (⌘-Option-Shift-D)

6. **VPN Troubleshooting**
   - Is VPN installed and up to date?
   - Can you see VPN servers? (DNS name resolution)
   - Can you connect to VPN? (authentication)
   - Can you reach internal resources? (routing after VPN)
   - Are there certificate warnings? (expiration, mismatch)

7. **Common Issues & Root Causes**
   - **"No Internet"** → WiFi off, DHCP failure, wrong password, DNS broken
   - **"Slow connection"** → Congestion, distance from AP, interference, ISP throttling
   - **"VPN won't connect"** → Outdated software, certificate expired, firewall blocking port
   - **"Intermittent drops"** → Interference, overheating, driver bug, cable damage
   - **"Can't reach server"** → DNS not resolving, firewall blocking, wrong IP

8. **Remote Support Tools & Techniques**
   - Remote assistance (Windows Quick Assist, TeamViewer)
   - Remote diagnostics (AnyDesk, Splashtop)
   - Logs and captures (packet captures with Wireshark)
   - Remote driver updates
   - Remote OS updates

9. **When to Escalate**
   - ISP-level issues (backbone congestion, DNS poisoning)
   - Firewall rule changes (security team decision)
   - Hardware failure (RMA required)
   - VPN provider issues (ticket with vendor)

10. **Documentation Template**
    ```
    Issue: [User's description]
    Symptom: [What they observe]
    Diagnosis: [Your findings]
    Root Cause: [Why it happened]
    Solution: [What you did]
    Verification: [How you confirmed it works]
    Prevention: [How to avoid in future]
    ```

11. **Metrics & Tracking**
    - Diagnosis time (target: < 15 min)
    - Resolution time (target: < 1 hour for most issues)
    - Recurrence rate (same user, same issue within 30 days)
    - Customer satisfaction

---

## KBA #5: New Employee IT Setup Checklist

**Target:** 800–1000 words  
**Audience:** HR, Onboarding Coordinators, IT Admins  
**Purpose:** Complete step-by-step workflow for adding new user to all systems  
**What it demonstrates:** Operational completeness, attention to compliance, customer service focus

### Outline

1. **Overview of Process**
   - Timeline: Pre-arrival (2 weeks), Day 1 (morning), Week 1 (ongoing)
   - Ownership: Who does what, escalation path
   - Verification: How to confirm completion

2. **Pre-Arrival (T-14 days)**
   - [ ] Receive new hire notification from HR
   - [ ] Create user directory (username, email alias schema)
   - [ ] Create Active Directory account
   - [ ] Create cloud storage account (Google Drive, OneDrive)
   - [ ] Create VPN credentials
   - [ ] Provision hardware (laptop, peripherals, setup)
   - [ ] Create email account & configure forwarding
   - [ ] Add to relevant security groups (based on department/role)
   - [ ] Prepare welcome packet (password reset link, support contact, first-day instructions)
   - [ ] Notify manager that hardware is being shipped

3. **Pre-Arrival (T-3 days)**
   - [ ] Configure laptop before shipment
     - [ ] Install OS and security patches
     - [ ] Install essential software (VPN, antivirus, collaboration apps)
     - [ ] Configure WiFi with WPA3 security
     - [ ] Test all core functions (network, VPN, email, storage)
   - [ ] Arrange delivery with new hire (confirm date/time)
   - [ ] Create welcome video or guide (optional, high-touch)
   - [ ] Brief manager on support plan

4. **Day 1 Morning (Welcome Call)**
   - [ ] Reach out via phone/Slack 30 min before scheduled arrival
   - [ ] Confirm delivery receipt
   - [ ] Walk through unboxing (check components)
   - [ ] Guide power-on and initial setup
   - [ ] Have new hire set password (secure environment, you don't set it)
   - [ ] Test WiFi connection from their location
   - [ ] Test VPN connection
   - [ ] Confirm email working
   - [ ] Brief on first-day agenda (team calls, document access, etc.)
   - [ ] Provide onboarding contact info (your cell, ticket system)
   - [ ] Book follow-up call for end of Day 1

5. **Day 1 (Ongoing Support)**
   - [ ] Be available for quick questions
   - [ ] Monitor email account for access issues
   - [ ] Follow up on any failed app logins
   - [ ] Prepare list of commonly-needed software (file requests)
   - [ ] Document any issues encountered

6. **End of Day 1**
   - [ ] Quick 15-min check-in call
   - [ ] Confirm systems are working
   - [ ] Address any urgent issues
   - [ ] Set expectations for Week 1 support

7. **Week 1 (Ongoing)**
   - [ ] Monitor for failed requests or access issues
   - [ ] Proactively reach out mid-week (not waiting for tickets)
   - [ ] Ensure all required apps are installed and working
   - [ ] Security training (password best practices, phishing awareness)
   - [ ] Review backup & recovery procedures
   - [ ] Confirm VPN usage from multiple locations (if applicable)

8. **End of Week 1**
   - [ ] New hire satisfaction survey
   - [ ] Confirm all access is working
   - [ ] Document any issues or improvements
   - [ ] Archive onboarding materials (for future reference)
   - [ ] Mark as "fully onboarded" in tracking system

9. **Post-Onboarding (Month 1)**
   - [ ] Check in at 1-week (proactive, not reactive)
   - [ ] Offer in-depth training if needed (Google Drive structure, VPN advanced features)
   - [ ] Gather feedback on IT setup experience (survey)
   - [ ] Make improvements based on feedback

10. **Checklist (Printable)**
    - [ ] Directory account created
    - [ ] Email active
    - [ ] Cloud storage provisioned
    - [ ] VPN credentials issued
    - [ ] Hardware shipped and received
    - [ ] Software installed
    - [ ] Network connectivity verified
    - [ ] Welcome materials sent
    - [ ] First-day call completed
    - [ ] Mid-week check-in completed
    - [ ] Week 1 survey completed
    - [ ] Issues resolved

11. **Communication Templates**
    - Pre-arrival welcome email
    - Day 1 support call script
    - Mid-week check-in message
    - End of week 1 survey link
    - Follow-up "any questions?" message

---

## Production Notes

**Format for all KBAs:**
- Title (H1)
- Audience + purpose (introduction)
- Clear sections with H2 headings
- Step-by-step numbered lists for procedures
- Checklists where applicable
- Visual aids (screenshots, flowcharts, decision trees)
- Tables for reference data
- Troubleshooting section
- "When to escalate" guidance
- Links to related KBAs

**Tone:**
- Professional but approachable
- Assume reader may have varying technical expertise
- Explain jargon on first use
- Give context before diving into steps
- End with "Still having issues? [Contact/Escalate]"

**Length target:** 800–1400 words (depth relative to complexity)

**Review checklist before publishing:**
- [ ] Steps are accurate and complete
- [ ] Screenshots/diagrams are clear and labeled
- [ ] Jargon is explained
- [ ] Tone is consistent and helpful
- [ ] Escalation path is clear
- [ ] Links to related KBAs are added
- [ ] No company-sensitive info exposed
