"""
PDF Schedule Parser -- [THEATER_NAME]
Parses leadership schedule PDFs using word positions.
Returns same format as schedule_parser.py (Excel version).
"""

import fitz
import re
from datetime import datetime, timedelta, date
from collections import defaultdict

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
SHIFT_MAP = {
    "6A-2":  (6,14), "6A-12": (6,12), "8A-4": (8,16), "10A-7": (10,19),
    "11A-7": (11,19),"11A-9": (11,21),"12P-9": (12,21),"1P-9":  (13,21),
    "2P-8":  (14,20),"2P-10": (14,22),"2P-12": (14,24),"4P-12": (16,24),
    "4P-X":  (16,26),"6A-4P": (6,16), "6P-X":  (18,26),"6P-12": (18,24),
    "7P-X":  (19,26),"8P-X":  (20,26),"10A-6": (10,18),"10A-8": (10,20),
    "12P-8": (12,20),"8A-6":  (8,18), "8A-4":  (8,16),
}
OFF_STRINGS = {"OFF","R/O","RO","VAC","VACATION","OUT"}
SEGMENT_ORDER = ["Morning","1st Shift","2nd Shift","3rd Shift",
                 "1st Evening","2nd Evening","3rd Evening"]
DOW_ORDER = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

DATE_RE = re.compile(r'(\d{2})/(\d{2})/(\d{2,4})')
SHIFT_RE = re.compile(r'^\d+[aApP][-–]\d+[aApPxX]?$|^\d+[aApP][-–][xX]$')

def normalize_shift(s):
    s = str(s).strip().upper().replace(' ','').replace('–','-')
    if not s or any(off in s for off in OFF_STRINGS): return None
    return s

def shift_to_hours(shift_str):
    key = normalize_shift(shift_str)
    if not key: return None
    if key in SHIFT_MAP: return SHIFT_MAP[key]
    try:
        if '-' not in key: return None
        start_s, end_s = key.split('-', 1)
        def ph(h, ref=None):
            h = h.strip()
            if h in ('X','26'): return 26
            sfx = ''
            if h and h[-1] in ('A','P'): sfx=h[-1]; h=h[:-1]
            v = int(h)
            if sfx=='P': return v if v==12 else v+12
            elif sfx=='A': return 0 if v==12 else v
            else:
                if ref and v < ref: return v+12
                return v
        s = ph(start_s); e = ph(end_s, ref=s)
        if e != 26 and e <= s: e += 12
        return (s, e)
    except: return None

def shift_covers_segment(shift_hours, seg_hours):
    if not shift_hours or not seg_hours: return False
    s, e = shift_hours; g, h = seg_hours
    return s < h and e > g

def get_rows(page, y_bucket=10):
    """Group words into rows by y-position."""
    words = page.get_text("words")
    rows = defaultdict(list)
    for x0, y0, x1, y1, word, *_ in words:
        rows[round(y0 / y_bucket) * y_bucket].append((x0, word.strip()))
    return {y: sorted(v, key=lambda w: w[0]) for y, v in rows.items()}

def find_date_columns(rows):
    """Find date strings and their x-positions to map columns to dates."""
    date_cols = {}
    for y, row_words in rows.items():
        dates_in_row = []
        for x, w in row_words:
            m = DATE_RE.match(w)
            if m:
                mo, da, yr = int(m.group(1)), int(m.group(2)), int(m.group(3))
                if yr < 100: yr += 2000
                try:
                    d = date(yr, mo, da)
                    dates_in_row.append((x, d))
                except: pass
        if len(dates_in_row) >= 4:
            for x, d in dates_in_row:
                date_cols[x] = d
            break
    return date_cols

def assign_to_column(x, date_cols, tolerance=35):
    """Find the nearest date column for an x position."""
    if not date_cols: return None
    best = min(date_cols.keys(), key=lambda cx: abs(cx - x))
    if abs(best - x) <= tolerance:
        return date_cols[best]
    return None

def parse_pdf_schedule(filepath):
    """Parse a PDF schedule and return attribution dict."""
    doc = fitz.open(filepath)
    page = doc[0]
    rows = get_rows(page)
    date_cols = find_date_columns(rows)

    if not date_cols:
        return None, {}

    ys = sorted(rows.keys())
    people = []
    i = 0
    while i < len(ys):
        y = ys[i]
        row = rows[y]

        name_words = [(x, w) for x, w in row if x < 100 and w[0].isupper()
                      and len(w) >= 2 and not any(c.isdigit() for c in w)
                      and w not in ('Senior','Leadership','Contact','Training','New','Guest','Metric','Payroll','Qtr','Total','Clean','Friendly','Quick','Group','Events')]

        if len(name_words) >= 2 and i+1 < len(ys):
            next_row = rows[ys[i+1]]
            role_words = [w for x, w in next_row if x < 100 and w in ROLE_PRIORITY]
            if role_words:
                role = role_words[0]
                full_name = ' '.join(w for _, w in sorted(name_words, key=lambda nw: nw[0]))

                shifts = {}
                for x, w in row:
                    norm = normalize_shift(w)
                    if norm and shift_to_hours(norm):
                        d = assign_to_column(x, date_cols)
                        if d:
                            dow = d.strftime('%A')
                            if dow not in shifts:
                                shifts[dow] = (w, d)

                people.append({
                    'name': full_name,
                    'role': role,
                    'priority': ROLE_PRIORITY[role],
                    'shifts': shifts,
                })
                i += 2
                continue
        i += 1

    doc.close()

    # Build attribution
    attribution = {}
    for person in people:
        for dow, (shift_str, shift_date) in person['shifts'].items():
            hrs = shift_to_hours(shift_str)
            if not hrs: continue
            for seg_name, seg_hrs in SEGMENT_HOURS.items():
                if shift_covers_segment(hrs, seg_hrs):
                    key = (shift_date, seg_name)
                    entry = attribution.setdefault(key, {'mod': None, 'supervisors': [], 'cls': [], 'all': []})
                    entry['all'].append((person['name'], person['role']))
                    if person['role'] in ('GM','MGR','FMM') and entry['mod'] is None:
                        entry['mod'] = person['name']
                    elif person['role'] == 'SUP':
                        if person['name'] not in entry['supervisors']:
                            entry['supervisors'].append(person['name'])
                    elif person['role'] == 'CREW LEAD':
                        if person['name'] not in entry['cls']:
                            entry['cls'].append(person['name'])

    day_dates = {}
    for (d, seg), info in attribution.items():
        dow = d.strftime('%A')
        day_dates[dow] = d

    return attribution, day_dates

def get_shift_owner(attribution, survey_date, segment_name):
    if not isinstance(survey_date, date):
        if hasattr(survey_date, 'date'): survey_date = survey_date.date()
        else: return None
    return attribution.get((survey_date, segment_name))

if __name__ == '__main__':
    import sys
    path = sys.argv[1]
    attr, dates = parse_pdf_schedule(path)
    print(f"Week dates: {dates}")
    print(f"\nPeople/shifts found: {len(set(info['mod'] for info in attr.values() if info['mod']))} MODs")
    print("\nSample attribution:")
    for (d, seg), info in sorted(attr.items())[:10]:
        if info['mod'] or info['supervisors']:
            print(f"  {d} {seg:<16} MOD={info['mod'] or 'NONE':<22} SUP={info['supervisors']}")
