# Three Demo Projects: Detailed Plans

These are quick, completable projects designed to prove you can handle eXp Realty's IT support work while generating portfolio evidence and KBAs.

---

## PROJECT 1: Help Desk Ticket Management System

**What it demonstrates:** Organizational thinking, categorization logic, SLA understanding, escalation judgment, customer communication  
**Time:** 2–3 hours  
**Deliverables:**
1. Google Sheet: Sample ticket system with 5 realistic tickets
2. PDF/Document: Flowchart showing triage and escalation logic
3. KBA: "Help Desk Ticket Management Best Practices" (1000–1200 words)

### Project Scope

**Google Sheet Structure:**

| Ticket ID | Date Submitted | Category | Priority | User Name | Issue | Status | First Response Time | Resolution Time | Notes | Escalation? |
|-----------|----------------|----------|----------|-----------|-------|--------|---------------------|-----------------|-------|------------|
| [auto-gen] | [date] | [from list] | [P1–P4] | [name] | [brief desc] | [Intake/Triage/In Progress/Resolved/Closed] | [time] | [time or pending] | [tech notes] | [yes/no/vendor] |

**5 Sample Tickets to Create:**

1. **Password Reset (P3 - Medium, Typical)**
   - New employee can't log in on Day 1
   - Category: Account
   - First response: User called in, immediate password reset link sent
   - Resolution: User reset password, confirmed access, closed
   - Resolution time: 15 minutes
   - Demonstrates: Quick wins, good documentation

2. **Hardware Issue (P2 - High, Requires Escalation)**
   - Laptop won't charge; battery not recognized in BIOS
   - Category: Hardware
   - Troubleshooting: Restart, BIOS reset, driver update attempted
   - Escalation: Vendor RMA required after diagnostic steps
   - Demonstrates: Diagnostic methodology, when to escalate

3. **Network Connectivity (P1 - Critical, Time-Sensitive)**
   - Remote employee can't connect to VPN, affecting entire day
   - Category: Network
   - Diagnosis: VPN certificate expired, reinstall required
   - Resolution: Guided reinstall over phone, verified access, 1-hour resolution
   - Demonstrates: Urgency handling, remote support, customer empathy

4. **Software Installation Request (P3 - Medium, Straightforward)**
   - User needs Adobe Acrobat for client work, current version is Reader
   - Category: Software
   - Approval required: Verify license available, IT admin approval
   - Deployment: Remote software push + verification call
   - Demonstrates: Process awareness, license management

5. **Email Not Syncing (P2 - High, Needs Investigation)**
   - Outlook won't sync email from past 2 days; calendar also affected
   - Category: Software
   - Diagnosis: OST file corruption suspected
   - Solution: Rename/repair OST file, resync
   - Follow-up: Monitor for recurrence
   - Demonstrates: Advanced troubleshooting, documentation of solution

**Flowchart to Create:**

```
Ticket Received
  ↓
[Categorize] → Hardware / Software / Account / Network / Other
  ↓
[Assign Priority]
  • Critical/P1 (network down, all users): 15 min response
  • High/P2 (productivity blocked): 1 hour response
  • Medium/P3 (workaround available): 4 hour response
  • Low/P4 (enhancement, non-urgent): 24 hour response
  ↓
[Route to Specialist] → Hardware → John, Software → Sarah, Account → Lisa, Network → Mike
  ↓
[Attempt First-Contact Resolution?]
  • Quick restart? → Yes → Verify → Close
  • Driver update? → Yes → Test → Close or Escalate
  • Can fix easily? → Yes → Document → Close
  • Blocked by policy/license/hardware? → No → Escalate
  ↓
[Escalate if Needed]
  • Vendor RMA? → Hardware team contact
  • License purchase? → Finance approval
  • Access/compliance? → Security review
  • Out of scope? → Back to submitter with explanation
  ↓
[Notify Customer] → Status update within promised SLA
  ↓
[Resolve & Document] → Link to KBA, note solution for future
  ↓
[Close Ticket] → Survey satisfaction → Archive
```

**Deliverable Format:**

1. **Google Sheet Link** (shared, with sample data already filled in)
   - Published as PDF for portfolio
   - One sheet for tickets, one sheet for priority/category legend

2. **Flowchart** (can be:)
   - Drawn in draw.io (simple SVG, exported as image)
   - Text-based in Markdown with ASCII art
   - Screenshot of Lucidchart/Miro

3. **KBA Article** 
   - Use template from 02_KBA_TEMPLATES.md
   - Include the actual flowchart
   - Use the 5 sample tickets as examples throughout
   - Add communication templates section

### How to Present This

**Portfolio text (for application/portfolio):**

> Created a sample help desk ticketing system demonstrating triage methodology, priority classification, and escalation logic. Modeled on eXp's likely workflow. Includes 5 realistic tickets across all categories (hardware, software, account, network), each documented with diagnosis steps and resolution time. Developed accompanying knowledge base article on ticket management best practices. **Demonstrates:** Process thinking, SLA adherence, customer communication, severity assessment.

---

## PROJECT 2: Dual-Boot Hardware Deployment & Configuration Guide

**What it demonstrates:** Hands-on technical depth, hardware knowledge, OS mastery, documentation ability, ability to handle multi-system environments  
**Time:** 3–4 hours (mostly documentation of existing hackintosh project)  
**Deliverables:**
1. Step-by-step installation guide (with screenshots/diagrams)
2. Hardware compatibility matrix/checklist
3. Troubleshooting decision tree
4. KBA: "Dual-Boot & Multi-OS Environment Management" (1000–1400 words)
5. KBA: "Hardware Deployment Checklist for Remote Teams" (800–1000 words)

### Project Scope

**What You'll Document from Your Hackintosh Project:**

1. **Hardware Inventory & Specs**
   - Your actual build: Lian Li O11 Vision, RTX 5080, Ryzen 9950X3D, MSI MPG X870E Edge Ti, etc.
   - Explain why each component was chosen (compatibility, performance, reliability)
   - Create a compatibility checklist
   - Note any gotchas or surprises (e.g., wireless receiver for RGB fans)

2. **BIOS Configuration Deep Dive**
   - Screenshot key BIOS pages (or detailed descriptions if you can't screenshot)
   - Explain XMP/DOCP and why it matters
   - Document secure boot settings per OS
   - Fan curve tuning (the wireless RGB fan challenge you solved)
   - Power management settings

3. **OS Installation Process**
   - Step-by-step for Windows (with or without screenshots)
   - Step-by-step for any secondary OS you run
   - Disk partitioning strategy
   - Boot loader management (which OS boots by default)
   - Boot order in UEFI

4. **Driver Installation**
   - Order matters (chipset first, then everything else)
   - Platform-specific drivers (Intel Management Engine, AMD Ryzen Master, etc.)
   - GPU drivers (NVIDIA driver suite)
   - NIC drivers for network connectivity
   - Storage controller drivers

5. **Wireless Peripheral Integration** (Your unique value-add)
   - The challenge: RGB fans with wireless receiver, BIOS constraints
   - Solution: L-Connect 3 software, firmware updates, driver load order
   - What didn't work (and why)
   - Troubleshooting flowchart for wireless device pairing

6. **Thermal Management & Optimization**
   - Your cooling solution: Tryx AIO + Lian Li TL wireless fans
   - Thermal compound application
   - Fan curve optimization (by OS, by workload)
   - Monitoring tools: HWInfo, Corsair Link, etc.
   - Temperature targets
   - Stress testing (Prime95, MemTest86, FurMark)

7. **Common Issues & Solutions** (from your own build experience)
   - What problems did you encounter?
   - Troubleshooting steps for each
   - Root causes and preventive measures
   - Links to relevant communities or documentation

**Deliverable Format:**

1. **Installation Guide (PDF/Markdown)**
   - Title page with your name and date
   - Table of contents
   - 5–8 sections covering checklist → BIOS → installation → drivers → optimization
   - Plenty of white space and clear section breaks
   - Either screenshots or detailed prose descriptions
   - Estimated read time: 30–45 minutes for someone attempting installation

2. **Hardware Compatibility Matrix (Google Sheet or Table)**
   - Columns: Component Category, Specific Part, Driver Support (Windows/Mac/Linux), Known Issues, Recommended Version
   - Rows: CPU, GPU, Motherboard, RAM, Storage, NIC, AIO, Fans, PSU, Case
   - Color-code: Green (fully compatible), Yellow (known quirks), Red (avoid)
   - Notes: Your personal experience with each component

3. **Troubleshooting Decision Tree (Flowchart)**
   - "System won't power on" → check PSU, BIOS battery
   - "Only one boot option visible" → check boot order, check EFI partition
   - "Fans spinning but no display" → check RAM seating, GPU seating
   - "Excessive heat after install" → fan curve not applied, thermal paste too thick
   - "Wireless peripherals unpaired after restart" → driver load order, L-Connect 3 not starting
   - etc.

4. **KBA #3: Dual-Boot & Multi-OS Environment Management**
   - Use the template from 02_KBA_TEMPLATES.md
   - Reference your actual build throughout
   - Include your BIOS settings as examples
   - Include your thermal optimization strategy
   - Add your troubleshooting decision tree as a visual

5. **KBA #1: Hardware Deployment Checklist**
   - Similar to above, but reframed for *deploying* hardware to users
   - "Before shipping," "unboxing," "week 1 validation"
   - Your build knowledge feeds into the "pre-delivery OS configuration" section
   - Document approach to driver installation, BIOS setup, thermal testing

### How to Present This

**Portfolio text:**

> Documented complete hardware build and dual-boot configuration process based on custom PC design (Lian Li O11 Vision, NVIDIA RTX 5080, AMD Ryzen 9950X3D, MSI X870E motherboard with wireless RGB fan integration). Includes step-by-step BIOS configuration, OS installation across multiple platforms, driver sequencing, and advanced thermal optimization. Created hardware compatibility matrix, troubleshooting decision tree, and detailed KBA article. **Demonstrates:** Deep technical depth, hardware troubleshooting, multi-OS competency, ability to document complex processes, attention to detail, and persistence in solving advanced configuration challenges.

---

## PROJECT 3: Remote Support Protocol & Runbook

**What it demonstrates:** Troubleshooting methodology, clear thinking, customer communication, process documentation, remote-first mindset  
**Time:** 2–3 hours  
**Deliverables:**
1. First-Time Troubleshooting Protocol (step-by-step flowchart/document)
2. "10 Common Issues & Quick Fixes" checklist
3. Email/Slack communication templates for support tickets
4. KBA: "Troubleshooting Remote Connectivity Issues" (900–1100 words)
5. KBA: "New Employee IT Setup Checklist" (800–1000 words)

### Project Scope

**Document 1: First-Time Troubleshooting Protocol**

Create a decision-tree document that walks through how to approach *any* support request:

1. **Initial Triage (on first contact)**
   ```
   Question: "What are you seeing?" (not what you expect, what they actually see)
   → Not seeing anything? → Power? → Restart?
   → Seeing an error? → Take screenshot → Google error message?
   → Thing used to work but doesn't now? → What changed? → Driver update? → Windows update?
   
   Question: "What have you already tried?"
   → Saves time, shows user has done basic troubleshooting
   
   Question: "When did this start?"
   → Correlation with OS update, software install, network change?
   
   After 3-5 questions, should have 80% confidence in diagnosis
   ```

2. **Diagnostic Path** (for common symptoms)
   ```
   Symptom: "No internet"
   1. Can you see WiFi networks? 
      → Yes → Can you connect?
         → Yes → Is there a browser? → Can you see websites?
         → No → Is WiFi password correct?
      → No → Is WiFi hardware on? (airplane mode, WiFi button)
   
   2. Ethernet alternative: Do you have an Ethernet port? Can you plug in?
      → Yes → Does that work? If yes → WiFi problem, not internet problem
   
   3. If both WiFi and Ethernet fail → ISP issue → Restart modem and router
   ```

3. **Remote Access Techniques**
   - Asking permission for remote access (Google Meet screen share? TeamViewer?)
   - Safe remote access practices (don't store passwords, confirm user is watching)
   - Tools available (Windows Remote Assist, Quick Assist, TeamViewer, AnyDesk)

4. **Documentation During Support**
   - What commands you ran
   - What you observed
   - What solution you applied
   - Link to relevant KBA (or create it after)
   - Next steps if issue recurs

5. **Escalation Decision**
   ```
   After 30 minutes of troubleshooting with no progress:
   → Is this a known issue? → Check KBA + Google
   → Is this a hardware issue? → Document symptoms → vendor support
   → Is this a security/compliance issue? → escalate to security team
   → Is this user-error? → Training + documentation, close
   → Is this beyond your scope? → Document and escalate with full context
   ```

**Document 2: 10 Common Issues & Quick Fixes**

Create a one-page cheat sheet:

```
1. "Forgot Password"
   → Send password reset link
   → User resets in secure environment
   → Done in 5 minutes
   SLA: 15 min response

2. "Computer won't turn on"
   → Is it plugged in?
   → Try different outlet
   → Hold power button 30 seconds (full discharge)
   → Try again
   SLA: If still not working → Hardware issue → escalate

3. "WiFi keeps disconnecting"
   → Forget and rejoin network
   → Update WiFi drivers
   → Change WiFi channel (if admin)
   → May be interference or weak signal
   SLA: 4 hours to attempt fix

4. "Email not syncing"
   → Force close email app
   → Restart device
   → Remove and re-add email account
   → If Outlook → restart Outlook sync
   SLA: 1 hour

5. "Application won't open"
   → Is it installed? (check Control Panel / Applications)
   → Try restart
   → Try uninstall/reinstall
   → Check system requirements
   SLA: 4 hours

6. "Printer not working"
   → Is printer on?
   → Is it on same network?
   → Try printing test page from printer settings
   → Restart printer
   → Restart computer
   SLA: 4 hours

7. "Slow computer / applications freezing"
   → Check Task Manager / Activity Monitor
   → Close unnecessary apps
   → Check available disk space
   → Run antivirus scan
   → May need hardware upgrade → escalate
   SLA: 4 hours investigation, then escalate if needed

8. "External drive not recognized"
   → Try different USB port
   → Try different cable
   → Check Device Manager / System Report
   → May need driver installation
   SLA: 1 hour

9. "Screen resolution wrong / display issues"
   → Check Settings → Display
   → Update video drivers
   → Try different cable (if external monitor)
   → Try different monitor (if possible)
   SLA: 4 hours

10. "VPN won't connect"
    → Is VPN software installed and up to date?
    → Try restart
    → Try different VPN server
    → Check if you have internet (VPN needs internet to start)
    → Certificate may be expired → check with vendor
    SLA: 1 hour, escalate if not vendor issue
```

**Document 3: Communication Templates**

Create templates for common scenarios:

1. **Initial Acknowledgment (within 5 min)**
   ```
   Hi [Name],
   
   Thanks for reaching out! I received your support request: [brief paraphrase of issue].
   
   I'm investigating this now and will follow up with next steps within [30 min / 1 hour / 4 hours, depending on priority].
   
   In the meantime, if you haven't already, please try [one quick suggestion].
   
   Best,
   [Your name]
   ```

2. **Status Update (if taking > 30 min)**
   ```
   Hi [Name],
   
   Still working on your issue. Here's what I've found so far:
   [One sentence about your diagnosis]
   
   Next step: [What you're trying next]
   
   I'll update you by [specific time].
   
   Thanks for your patience!
   ```

3. **Resolution Confirmation**
   ```
   Hi [Name],
   
   Good news! I've resolved your issue. Here's what was happening and what I fixed:
   
   Problem: [What was broken]
   Root cause: [Why it happened]
   Solution: [What I did]
   
   To prevent this in the future: [Preventive steps]
   
   Please confirm everything is working on your end. Reply with any questions!
   
   Cheers,
   [Your name]
   ```

4. **Escalation Notice**
   ```
   Hi [Name],
   
   I've been investigating your issue ([brief desc]) and determined this needs expertise beyond my current toolset. 
   
   Here's what I've found:
   [Your diagnostic steps]
   [Your observations]
   
   Next steps: I'm escalating to [Team/Vendor] who specialize in [area]. They'll reach out within [timeframe].
   
   I'll stay looped in and follow up with you once they have a solution.
   
   Thanks for your patience!
   ```

5. **Ticket Closure Survey**
   ```
   Hi [Name],
   
   Your support ticket (#[ID]) has been marked as resolved. 
   
   Would you mind taking 30 seconds to rate your experience?
   → [Link to 1-min survey]
   
   Your feedback helps us improve!
   
   Thanks,
   [Your name]
   ```

**KBA Articles:**

4. **KBA #4: Troubleshooting Remote Connectivity Issues**
   - Use the template from 02_KBA_TEMPLATES.md
   - Include your diagnostic flowchart
   - Windows and Mac-specific commands
   - VPN troubleshooting section
   - When to escalate section

5. **KBA #5: New Employee IT Setup Checklist**
   - Complete pre-arrival, day 1, week 1, and month 1 timeline
   - Checklists for each phase
   - Communication templates for each milestone
   - Metrics to track (onboarding satisfaction, time to productivity)
   - Feedback loop for continuous improvement

### How to Present This

**Portfolio text:**

> Created a comprehensive remote support protocol documenting first-contact troubleshooting methodology, escalation criteria, and customer communication framework. Includes diagnostic flowchart for any support scenario, "10 quick fixes" cheat sheet for common issues, and templated responses for typical ticket lifecycle moments. Developed accompanying KBAs on remote connectivity and new-hire onboarding. **Demonstrates:** Systematic thinking, user empathy, clear communication, documented processes, remote-first approach, and ability to turn experience into reusable knowledge.

---

## Summary: What You'll Have After These Three Projects

**Tangible Deliverables:**
- 3 Google Sheets (tickets, hardware matrix, onboarding checklist)
- 2 flowcharts/diagrams (ticket triage, troubleshooting decision tree)
- 5 complete KBA articles (1000–1400 words each)
- 1 hardware installation guide (500–1000 words)
- 3 communication templates (for different ticket scenarios)

**Portfolio Value:**
- Demonstrates depth across help desk operations, hardware, and software
- Shows writing ability and process thinking
- Proves you can handle eXp's core responsibilities
- Gives you concrete examples to reference in interviews
- Creates a knowledge base you can actually use in the job

**Time Investment:** ~8–10 hours total over 1–2 weeks

**Application Strategy:** 
- Submit resume + cover letter
- Include portfolio link or PDF samples of projects
- In cover letter, briefly reference the projects: "I've documented my approach to help desk management, hardware deployment, and remote support — included in my portfolio"
- Be ready to discuss each project in phone screening

---

## Execution Order (Recommended)

1. **Week 1, Day 1–2:** Project 1 (Ticket system) — easiest to start, builds momentum
2. **Week 1, Day 3–4:** Project 2 (Hardware guide) — uses your existing knowledge, feels natural
3. **Week 1/2, Day 5–6:** Project 3 (Remote support) — wraps everything together
4. **Between projects:** Draft KBAs incrementally as you finish each project
5. **Final polish:** Proofread, collect feedback, finalize resume + cover letter
6. **Apply:** Submit complete package to eXp Realty

**Budget:** 2–3 hours/day for 4–5 days → deliverables ready by end of Week 1
