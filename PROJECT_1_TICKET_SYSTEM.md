# PROJECT 1: Help Desk Ticket Management System

**Objective:** Create a working help desk ticketing system with realistic sample data demonstrating triage, escalation, and SLA management.

**Deliverables:**
1. Google Sheet: Sample ticket management system
2. Flowchart: Triage and escalation logic
3. Communication templates
4. KBA: Help Desk Ticket Management Best Practices

**Time to Complete:** 2–3 hours  
**Status:** Ready to build

---

## PART 1: Google Sheet Setup

### Sheet Structure

Create a new Google Sheet named **"Help Desk Ticket System - Sample Data"** with this structure:

**Column Headers (Row 1):**
```
Ticket ID | Date Submitted | Category | Priority | User Name | Issue Summary | Status | Assigned To | First Response Time | Resolution Time | Notes | Escalated?
```

### Sample Ticket Data (5 Realistic Examples)

Copy/paste these into your Google Sheet starting at Row 2:

---

**TICKET 1: Password Reset (Quick Win)**

| Field | Value |
|-------|-------|
| Ticket ID | TKT-001 |
| Date Submitted | 2026-06-02 09:15 AM |
| Category | Account |
| Priority | P3 (Medium) |
| User Name | Sarah Chen |
| Issue Summary | Cannot log in to company portal; forgot password |
| Status | Resolved |
| Assigned To | Help Desk - Khris |
| First Response Time | 5 minutes |
| Resolution Time | 12 minutes |
| Notes | User called in at 9:15 AM. Sent password reset link via email. User reset password in secure environment. Confirmed access to portal. Closed. |
| Escalated? | No |

---

**TICKET 2: Hardware Issue (Escalation)**

| Field | Value |
|-------|-------|
| Ticket ID | TKT-002 |
| Date Submitted | 2026-06-01 14:22 PM |
| Category | Hardware |
| Priority | P2 (High) |
| User Name | Marcus Johnson |
| Issue Summary | Laptop won't charge; battery not recognized in BIOS |
| Status | Escalated to Vendor |
| Assigned To | Help Desk - Khris |
| First Response Time | 22 minutes |
| Resolution Time | 4 hours (escalation pending) |
| Notes | User reported laptop won't charge after OS update. Troubleshooting: (1) Tried different outlets - no change. (2) Restarted laptop - battery still unrecognized. (3) Checked BIOS - no battery detected. (4) Updated chipset drivers - no change. (5) Attempted BIOS reset - issue persists. Diagnosis: Likely hardware failure (charger port or battery connector). Escalated to vendor for RMA. Awaiting approval. |
| Escalated? | Yes - Vendor RMA |

---

**TICKET 3: Network/VPN (Critical, Time-Sensitive)**

| Field | Value |
|-------|-------|
| Ticket ID | TKT-003 |
| Date Submitted | 2026-06-02 08:47 AM |
| Category | Network |
| Priority | P1 (Critical) |
| User Name | Jennifer Martinez |
| Issue Summary | Cannot connect to VPN; blocking all remote work |
| Status | Resolved |
| Assigned To | Help Desk - Khris |
| First Response Time | 4 minutes |
| Resolution Time | 38 minutes |
| Notes | Critical: User WFH and unable to access internal systems. Called in at 8:47 AM. Quick diagnostics: (1) VPN software installed? Yes. (2) VPN certificate expired? Check — yes, certificate expired 2 days ago. (3) Solution: Had user uninstall VPN client, cleared cache, reinstalled latest version with updated certificate. (4) User tested connectivity — successful. (5) Confirmed access to internal resources. Closed at 9:25 AM. Follow-up: Sent user KB article on VPN certificate renewal to prevent future issues. |
| Escalated? | No |

---

**TICKET 4: Software Installation (Requires Approval)**

| Field | Value |
|-------|-------|
| Ticket ID | TKT-004 |
| Date Submitted | 2026-06-01 11:33 AM |
| Category | Software |
| Priority | P3 (Medium) |
| User Name | David Lee |
| Issue Summary | Need Adobe Acrobat Pro for client deliverables; currently have Reader only |
| Status | In Progress |
| Assigned To | Help Desk - Khris |
| First Response Time | 45 minutes |
| Resolution Time | 2 hours (pending approval) |
| Notes | User needs Adobe Acrobat Pro to edit PDFs for client work. (1) Verified: Company has 5 available licenses, user not currently licensed. (2) Submitted license request to Finance for approval. (3) Awaiting approval before deployment. User priority: Medium (workaround available: external PDF editing tools). Will deploy upon approval. |
| Escalated? | Yes - Finance approval |

---

**TICKET 5: Email Sync Issue (Investigation Required)**

| Field | Value |
|-------|-------|
| Ticket ID | TKT-005 |
| Date Submitted | 2026-06-02 10:14 AM |
| Category | Software |
| Priority | P2 (High) |
| User Name | Rebecca Wilson |
| Issue Summary | Outlook not syncing email; missing past 2 days of messages and calendar events |
| Status | Resolved |
| Assigned To | Help Desk - Khris |
| First Response Time | 8 minutes |
| Resolution Time | 1 hour 22 minutes |
| Notes | User reported Outlook stopped syncing yesterday morning. Email and calendar affected. Troubleshooting: (1) Closed Outlook completely. (2) Checked OST file size — 1.8GB, larger than normal. (3) Navigated to C:\Users\rebecca.wilson\AppData\Local\Microsoft\Outlook\ (4) Renamed old rebecca.wilson@company.ost to .backup. (5) Restarted Outlook — new OST created and began syncing. (6) Monitored sync progress — took 22 minutes to download all 2 days of messages. (7) Verified calendar and email working. (8) Confirmed with user — all data recovered. Root cause: OST file corruption (likely from unexpected shutdown). Solution: OST rebuild. Prevention: Proper shutdown procedures. Closed. |
| Escalated? | No |

---

## PART 2: Categorization & Priority Legend

Create a second sheet named **"Reference - Categories & Priorities"** with this data:

### Categories

| Category | Definition | Examples | Primary Owner |
|----------|-----------|----------|----------------|
| **Account** | User access, credentials, permissions | Password reset, account lockout, new user setup, access request | IT Admin |
| **Software** | Application installation, licensing, bugs | Install request, license renewal, app won't open, sync issues | Software Support |
| **Hardware** | Device failure, peripherals, physical issues | Laptop won't charge, monitor broken, keyboard not working | Hardware Tech |
| **Network** | Connectivity, VPN, internet, WiFi | Can't connect to internet, VPN won't connect, slow network | Network Team |
| **Other** | Doesn't fit above categories | Facilities issue, HR question, vendor issue | Route to appropriate team |

### Priority Levels

| Priority | Response SLA | Resolution SLA | Examples |
|----------|-------------|----------------|----------|
| **P1 - Critical** | 15 minutes | 2 hours | Network down, all users affected, VPN won't connect, can't access email |
| **P2 - High** | 1 hour | 4 hours | Productivity blocked, multiple users affected, hardware failure, major app bug |
| **P3 - Medium** | 4 hours | 8 hours | Isolated user, workaround available, non-critical software |
| **P4 - Low** | 24 hours | 48 hours | Enhancement request, minor bug, cosmetic issue |

### Status Workflow

| Status | Meaning |
|--------|---------|
| **New** | Just submitted, waiting for triage |
| **Triage** | Initial assessment in progress |
| **In Progress** | Actively working on resolution |
| **Escalated** | Handed off to specialist or vendor |
| **Waiting on Customer** | Awaiting response from user |
| **Resolved** | Solution applied, awaiting closure confirmation |
| **Closed** | Confirmed resolved, ticket archived |

---

## PART 3: Triage Flowchart (Text Version)

Use this flowchart to guide triage decisions:

```
TICKET RECEIVED
↓
CATEGORIZE
├─ Is it hardware? → HARDWARE (escalate if failure)
├─ Is it software/app? → SOFTWARE
├─ Is it account/access? → ACCOUNT
├─ Is it network/connectivity? → NETWORK
└─ Other? → OTHER (route appropriately)
↓
ASSIGN PRIORITY
├─ Affects multiple users or core service? → P1 (Critical)
├─ Affects one user, blocks productivity? → P2 (High)
├─ Affects one user, workaround exists? → P3 (Medium)
└─ Enhancement or low impact? → P4 (Low)
↓
ROUTE TO ASSIGNEE (based on category)
↓
FIRST RESPONSE (within SLA)
├─ Can fix in 5-10 min? (restart, password reset, etc.) → ATTEMPT
├─ Requires specialist? → ESCALATE
└─ User action needed? → REQUEST & WAIT
↓
RESOLUTION (within SLA)
├─ Fixed? → DOCUMENT & CLOSE
├─ Not fixed? → ESCALATE
└─ Waiting on customer? → FOLLOW UP
```

---

## PART 4: Communication Templates

### Template 1: Initial Acknowledgment

```
Subject: [TKT-###] Support Request Received

Hi [User Name],

Thank you for reaching out. I've received your support request regarding [brief description of issue].

**Ticket #:** [TKT-###]
**Priority:** [P1/P2/P3/P4]
**Category:** [Category]

I'm investigating this now and will provide an update within [SLA time] with next steps.

In the meantime, if you haven't already, please try:
[One quick suggestion relevant to their issue]

I'll be in touch shortly.

Best regards,
[Your Name]
Help Desk Support
[Contact Info]
```

### Template 2: Status Update (if resolving > 30 min)

```
Subject: [TKT-###] Status Update

Hi [User Name],

Still working on your issue. Here's what I've found so far:

**What I've checked:**
- [Diagnostic step 1]
- [Diagnostic step 2]
- [Finding or hypothesis]

**Next steps:**
- [What you're trying next]

I'll follow up by [specific time] with either a solution or next steps.

Thanks for your patience!

Best regards,
[Your Name]
```

### Template 3: Resolution Confirmation

```
Subject: [TKT-###] Issue Resolved

Hi [User Name],

Good news! I've resolved your issue. Here's what was happening and what I fixed:

**Problem:** [What was broken]
**Root Cause:** [Why it happened]
**Solution Applied:** [What I did step-by-step]
**Verification:** [How I confirmed it works]

**To prevent this in the future:**
[Preventive steps or best practices]

Please confirm that everything is working on your end. Reply if you have any questions!

Best regards,
[Your Name]
```

### Template 4: Escalation Notice

```
Subject: [TKT-###] Escalating Your Request

Hi [User Name],

I've been investigating your issue and determined it requires expertise beyond my current toolset.

**What I found:**
- [Your diagnostic findings]
- [What you tried and results]

**Next steps:**
I'm escalating to [Team/Vendor Name] who specialize in this area. They'll reach out within [timeframe].

I'll stay looped in and follow up with you once we have a solution.

Thanks for your patience!

Best regards,
[Your Name]
```

### Template 5: Ticket Closure Survey

```
Subject: [TKT-###] Help Us Improve

Hi [User Name],

Your support ticket has been marked as resolved!

Would you mind taking 1 minute to rate your experience? Your feedback helps us improve our support:

[Rate your experience: 1-5 stars]
[Comments]

→ [Link to survey or reply with rating]

Thank you!

[Your Name]
```

---

## PART 5: Key Metrics to Track

Track these metrics to demonstrate your effectiveness:

| Metric | Target | Formula |
|--------|--------|---------|
| **Average First Response Time** | < 30 min | (Sum of all response times) / (number of tickets) |
| **Average Resolution Time** | < 4 hours | (Sum of all resolution times) / (number of tickets) |
| **First-Contact Resolution Rate** | > 60% | (Tickets resolved without escalation) / (total tickets) × 100 |
| **Customer Satisfaction** | > 4.5/5 | Average of survey responses |
| **Ticket Volume** | Track trend | Count of tickets per week/month |
| **Escalation Rate** | < 20% | (Escalated tickets) / (total tickets) × 100 |

---

## How to Implement This

### Step 1: Create Google Sheet (15 min)
1. Go to Google Sheets
2. Create new sheet named "Help Desk Ticket System - Sample Data"
3. Copy the column headers from Part 1
4. Paste in the 5 sample tickets with all their data
5. Create second sheet "Reference - Categories & Priorities" with lookup tables

### Step 2: Format & Aesthetics (15 min)
- Freeze header row
- Color-code priority levels (P1=Red, P2=Orange, P3=Yellow, P4=Green)
- Color-code status (New=Gray, In Progress=Blue, Escalated=Orange, Resolved=Green, Closed=Black text)
- Make it easy to scan visually
- Add borders and gridlines

### Step 3: Create Flowchart (30 min)
- Use draw.io (free, online)
- Recreate the triage flowchart from Part 3
- Export as PNG/PDF
- Save to your project folder

### Step 4: Save URLs
- Share Google Sheet link (can be view-only)
- Save flowchart image

### Step 5: Reference in Portfolio
Include these in your portfolio with caption:
> "Help Desk Ticket Management System - Created a realistic ticketing system with 5 sample tickets demonstrating triage methodology, priority assignment, escalation logic, and SLA management. Includes reference tables, communication templates, and visual flowchart showing decision logic."

---

## What This Demonstrates

✅ **Process thinking** — categorization, priority framework, SLA awareness  
✅ **Customer communication** — professional templates for all scenarios  
✅ **Operational excellence** — metrics tracking, documentation, escalation criteria  
✅ **Real-world readiness** — sample tickets are realistic and based on actual help desk scenarios  
✅ **Attention to detail** — structured approach, documentation standards, follow-up  

---

## Next: KBA Article

Once this is complete, you'll write **KBA Article: Help Desk Ticket Management Best Practices** that references these 5 tickets and explains the methodology in depth. The KBA is the deeper, educational version of this practical system.

---

## Time Estimate

- Google Sheet setup: 30 minutes
- Flowchart creation: 30 minutes
- Document review & polish: 15 minutes
- **Total: ~1 hour 15 minutes**

Start here — this is your quick win to build momentum!
