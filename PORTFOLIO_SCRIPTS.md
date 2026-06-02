# Python Scripts Portfolio

## Overview
Four interconnected Python scripts that automate customer satisfaction survey analysis and leadership attribution for operational management. Developed independently to solve real business problems at scale.

---

## Script 1: `backfill_gc_history.py`
**Purpose:** Historical data pipeline for survey backfill

**What it does:**
- Reads YTD customer satisfaction survey exports (Excel)
- Loads leadership schedules (PDF or Excel)
- Parses schedules and extracts shift coverage details
- Attributes each survey response to the manager/supervisor on duty that day
- Generates weekly JSON summaries for system import

**Key Skills Demonstrated:**
- Multi-source data integration (Excel + PDF)
- Complex attribution logic (matching surveys to people based on dates + time segments)
- Modular design (delegates to helper scripts)
- Data transformation and JSON generation
- Error handling and logging

**Dependencies:**
- openpyxl (Excel parsing)
- Custom: `schedule_parser`, `pdf_schedule_parser`

**Output:** JSON files per week + combined history file for bulk import

---

## Script 2: `generate_gc_report.py`
**Purpose:** Automated weekly reporting and analytics

**What it does:**
- Reads survey data from Excel export
- Calculates satisfaction percentages (% rating 4+ out of 5)
- Breaks down scores by metric (Friendly, Quick, Clean)
- Compares week-over-week trends
- Extracts top failure points from open-ended feedback
- Attributes scores to individual leaders
- Generates three formatted reports:
  1. **Crew Post** — Internal communication (Workvivo platform)
  2. **Leadership Email** — Overview with trends and coaching priorities
  3. **Shift Tracker** — Per-shift breakdown for coaching conversations

**Key Skills Demonstrated:**
- Complex data aggregation (multiple groupings: week, month, year, leader, shift)
- Trend analysis (week-over-week comparison)
- Natural language processing (filtering "noise" from feedback)
- Formatting for multiple audiences (crew, leadership, coaching)
- Integration with external system (Workvivo)
- PII handling (survey exports are sanitized to remove guest names, emails, addresses)

**Dependencies:**
- openpyxl (Excel)
- datetime (time-based filtering)
- Custom: `schedule_parser`, `pdf_schedule_parser` (optional)

**Output:** TXT files ready for distribution + JSON for system import

---

## Script 3: `pdf_schedule_parser.py`
**Purpose:** Extract leadership schedule from PDF documents

**What it does:**
- Uses PyMuPDF to extract text from PDF
- Groups words by y-position to reconstruct table structure
- Detects date columns by pattern matching
- Extracts person names and roles
- Parses shift times (8A-4, 6P-X, etc.)
- Maps each person to the time segments they cover
- Returns structured attribution (who was working which shift)

**Key Skills Demonstrated:**
- PDF parsing without pre-structured extraction
- Coordinate-based text reconstruction
- Regex pattern matching for dates and shifts
- Shift-to-segment mapping logic
- Error resilience (gracefully handles malformed PDFs)

**Dependencies:**
- fitz (PyMuPDF) — PDF text extraction
- re — Pattern matching
- datetime — Date parsing

**Key Challenge Solved:**
- PDFs don't have structured data like Excel; this script reconstructs the table by position
- Converts different shift formats (6A-2, 2P-10, 6P-X) to 24-hour ranges
- Maps shifts to business segments (Morning 0-12, 1st Shift 12-14, etc.)

**Output:** Attribution dict keyed by (date, segment) → {mod, supervisors, crew_leads}

---

## Script 4: `schedule_parser.py`
**Purpose:** Extract leadership schedule from Excel documents

**What it does:**
- Reads Excel workbook (sheet: "Leadership Schedule")
- Finds the Friday base date from the spreadsheet
- Calculates all week dates (Fri-Thu)
- Parses person names and roles from rows
- Extracts shift times for each day from columns
- Normalizes shift formats to 24-hour ranges
- Determines which shifts cover which business segments
- Returns same attribution structure as PDF parser

**Key Skills Demonstrated:**
- Excel workbook parsing (openpyxl)
- Sheet structure assumption and validation
- Date calculation (7-day week from Friday)
- Shift time normalization (handles multiple formats)
- Role prioritization (GM > MGR > FMM > SUP > CREW LEAD)
- Consistent interface (same output as PDF parser)

**Dependencies:**
- openpyxl — Excel parsing
- datetime — Date math

**Design Pattern:**
- Both PDF and Excel parsers return identical data structure
- Scripts can call either parser without knowing source format
- `backfill_gc_history.py` delegates to correct parser automatically

**Output:** Attribution dict keyed by (date, segment) → {mod, supervisors, crew_leads}

---

## How They Work Together

```
Input Data:
  - Survey Export (Excel): [date, segment, metric_1, metric_2, metric_3, feedback, ...]
  - Schedule (PDF or Excel): [names, roles, shifts by day]

Processing Pipeline:
  1. backfill_gc_history.py or generate_gc_report.py START
  2. Load survey data → filter by date range
  3. Load schedule → determine who was working
  4. → schedule_parser.py OR pdf_schedule_parser.py (auto-selected)
       ↓ Return: (date, segment) → {mod, supervisors, ...}
  5. Attribute each survey to the manager on duty
  6. Calculate scores by: week, leader, shift, metric
  7. Generate reports and JSON for import

Output:
  - crew_post.txt (internal comms)
  - leadership_email.txt (overview + trends)
  - shift_tracker.txt (coaching tool)
  - weekly_data.json (system import)
  - Full history JSON (bulk backfill)
```

---

## Technical Highlights

**Data Structures:**
- Survey attribution: `{(date, segment): {mod: str, supervisors: [str], cls: [str]}}`
- Scores: Calculated by filtering responses where rating >= 4, dividing by total valid responses
- Trends: Week-over-week deltas, MTD aggregates, YTD aggregates

**Edge Cases Handled:**
- Malformed shifts (6A-2 vs 6a-2 vs 6A–2 with different dash character)
- Boundary conditions (e.g., 11P close shifts that wrap into next day)
- Missing data (survey with no date, schedule with no role)
- PII sanitization (survey data is pre-cleaned before processing)

**Performance Considerations:**
- Assumes schedule files are relatively small (< 1000 people)
- Survey export can be large (thousands of responses) — filtered by date before scoring
- PDF parsing is slower than Excel; uses PDF fallback for archival schedules

---

## Skills Summary

This portfolio demonstrates:
- ✅ **Data pipeline design** — multi-stage ETL from raw exports to formatted reports
- ✅ **File format parsing** — Excel, PDF, JSON; flexible input handling
- ✅ **Complex business logic** — shift matching, attribution, score calculation
- ✅ **Code modularity** — reusable parsers, clear interfaces between scripts
- ✅ **Error handling** — graceful degradation for malformed inputs
- ✅ **Automation mindset** — reduces manual reporting from hours to seconds
- ✅ **Operational thinking** — understands time segments, role hierarchies, reporting needs
- ✅ **Problem-solving** — solved PDF extraction challenge without external dependencies

---

## How This Applies to IT Support

**Similar Skills in Help Desk:**
- Multi-source ticket data (email, phone, web, walk-ins) → unified triage
- Complex routing logic (priority + category → correct team)
- Attribution (ticket → technician, based on skill/availability)
- Trend analysis (response times, resolution rates, SLA compliance)
- Reporting (crew post → management overview; shift tracker → coaching)

This demonstrates the ability to **build systems that reduce manual work and improve visibility** — exactly what IT support needs.

---

## Files Included

1. `SCRIPT_1_backfill_gc_history.py` — Historical data backfill pipeline
2. `SCRIPT_2_generate_gc_report.py` — Weekly reporting automation
3. `SCRIPT_3_pdf_schedule_parser.py` — PDF schedule extraction
4. `SCRIPT_4_schedule_parser.py` — Excel schedule extraction
5. `PORTFOLIO_SCRIPTS.md` — This document

All scripts are production-ready and have been sanitized to remove theater names and internal system references.
