"""
Schedule Parser -- [THEATER_NAME]
Reads the weekly leadership schedule Excel and returns shift coverage
so survey scores can be attributed to the MOD on each shift.

Usage:
    from schedule_parser import parse_schedule
    schedule = parse_schedule("path/to/schedule.xlsx")
    # schedule = { date: { segment: { "mod": name, "supervisors": [...], "cls": [...] } } }
"""

import openpyxl
from datetime import datetime, timedelta, date

# Day columns in the schedule Excel (0-based col index)
DAY_COLS  = [5, 7, 9, 11, 13, 15, 17]
DAY_NAMES = ["Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"]

ROLE_PRIORITY = {"GM": 1, "MGR": 2, "FMM": 3, "SUP": 4, "CREW LEAD": 5}

SEGMENT_HOURS = {
    "Morning":     (0,  12),
    "1st Shift":   (12, 14),
    "2nd Shift":   (14, 16),
    "3rd Shift":   (16, 18),
    "1st Evening": (18, 20),
    "2nd Evening": (20, 22),
    "3rd Evening": (22, 26),
}

# Explicit shift time lookup (normalized to uppercase, spaces stripped)
SHIFT_MAP = {
    "6A-2":  (6,  14),
    "6A-12": (6,  12),
    "8A-4":  (8,  16),
    "10A-7": (10, 19),
    "11A-7": (11, 19),
    "12P-9": (12, 21),
    "1P-9":  (13, 21),
    "2P-10": (14, 22),
    "4P-12": (16, 24),
    "4P-X":  (16, 26),
    "6P-12": (18, 24),
    "6P-X":  (18, 26),
    "7P-X":  (19, 26),
    "8P-X":  (20, 26),
}

OFF_STRINGS = {"OFF", "R/O", "RO", "VACATION", "OUT"}


def normalize_shift(s):
    """Normalize a shift string for lookup."""
    if not s:
        return None
    s = str(s).strip().upper().replace(" ", "")
    if any(off in s for off in OFF_STRINGS):
        return None
    s = s.replace("A-", "A-").replace("P-", "P-")
    return s


def shift_to_hours(shift_str):
    """Convert a shift string like '8a-4' to (start_hour, end_hour) in 24h."""
    key = normalize_shift(shift_str)
    if not key:
        return None

    if key in SHIFT_MAP:
        return SHIFT_MAP[key]

    try:
        if "-" not in key:
            return None
        start_s, end_s = key.split("-", 1)

        def parse_h(h, ref=None):
            h = h.strip()
            if h in ("X", "26"):
                return 26
            suffix = ""
            if h and h[-1] in ("A", "P"):
                suffix = h[-1]
                h = h[:-1]
            val = int(h)
            if suffix == "P":
                return val if val == 12 else val + 12
            elif suffix == "A":
                return 0 if val == 12 else val
            else:
                if ref is not None and val < ref:
                    return val + 12
                return val

        start = parse_h(start_s)
        end   = parse_h(end_s, ref=start)
        if end <= start and end != 26:
            end += 12
        return (start, end)
    except Exception:
        return None


def shift_covers_segment(shift_hours, seg_hours):
    """True if the shift overlaps with the segment."""
    if not shift_hours or not seg_hours:
        return False
    s_start, s_end = shift_hours
    g_start, g_end = seg_hours
    return s_start < g_end and s_end > g_start


def parse_schedule(filepath):
    """
    Parse the leadership schedule Excel.

    Returns:
        { (date_obj, segment_name): { "mod": str, "supervisors": [str], "cls": [str] } }
    """
    wb = openpyxl.load_workbook(filepath, read_only=True)
    ws = wb["Leadership Schedule"]
    rows = list(ws.iter_rows(values_only=True))

    # Find the Friday base date
    base_friday = None
    for row in rows[:15]:
        for cell in row[4:8]:
            if isinstance(cell, datetime):
                base_friday = cell.date()
                break
        if base_friday:
            break

    if not base_friday:
        raise ValueError("Could not find week start date in schedule. "
                         "Make sure the Excel has the Friday date filled in.")

    # Build date map: day_name -> actual date
    day_dates = {}
    for i, day_name in enumerate(DAY_NAMES):
        day_dates[day_name] = base_friday + timedelta(days=i)

    # Parse people
    people = []
    i = 0
    while i < len(rows):
        row = rows[i]
        name = row[1] if len(row) > 1 else None
        if not name or str(name).strip() in ("", "Leadership", "Senior Leadership",
                                              "GM", "MGR", "SUP", "FMM", "CREW LEAD"):
            i += 1
            continue

        # Check next row for role
        role_row = rows[i + 1] if i + 1 < len(rows) else None
        role = role_row[1].strip().upper() if (role_row and role_row[1]) else None

        if role not in ROLE_PRIORITY:
            i += 1
            continue

        # Extract shift strings for each day
        shifts = {}
        for col, day in zip(DAY_COLS, DAY_NAMES):
            if col < len(row):
                raw = row[col]
                key = normalize_shift(raw)
                if key:
                    shifts[day] = str(raw).strip()

        people.append({
            "name": str(name).strip(),
            "role": role,
            "priority": ROLE_PRIORITY[role],
            "shifts": shifts,
        })
        i += 2

    # Build attribution: (date, segment) -> {mod, supervisors, cls, all}
    attribution = {}

    all_dates = list(day_dates.values())
    all_segs  = list(SEGMENT_HOURS.keys())

    for day_name, day_date in day_dates.items():
        for seg_name, seg_hrs in SEGMENT_HOURS.items():
            key = (day_date, seg_name)
            on_shift = []
            for p in people:
                shift_str = p["shifts"].get(day_name)
                if not shift_str:
                    continue
                hrs = shift_to_hours(shift_str)
                if hrs and shift_covers_segment(hrs, seg_hrs):
                    on_shift.append(p)

            # Sort by priority
            on_shift.sort(key=lambda p: p["priority"])

            mod = None
            supervisors = []
            cls = []

            for p in on_shift:
                if p["role"] in ("GM", "MGR", "FMM") and mod is None:
                    mod = p["name"]
                elif p["role"] == "SUP":
                    supervisors.append(p["name"])
                elif p["role"] == "CREW LEAD":
                    cls.append(p["name"])

            attribution[key] = {
                "mod":         mod,
                "supervisors": supervisors,
                "cls":         cls,
                "all":         [(p["name"], p["role"]) for p in on_shift],
            }

    return attribution, day_dates


def get_shift_owner(attribution, survey_date, segment_name):
    """Look up who owned a specific shift by date + segment."""
    if not isinstance(survey_date, date):
        if hasattr(survey_date, "date"):
            survey_date = survey_date.date()
        else:
            return None
    key = (survey_date, segment_name)
    return attribution.get(key)


if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else "schedule.xlsx"
    attr, dates = parse_schedule(path)
    print("Week dates:", dates)
    print("\nShift attribution sample:")
    for (d, seg), info in sorted(attr.items())[:14]:
        if info["mod"] or info["supervisors"]:
            print(f"  {d} {seg:<16} MOD={info['mod'] or 'NONE':<20} "
                  f"SUP={info['supervisors']} CL={info['cls']}")
