"""
Guest Satisfaction History Backfill -- [THEATER_NAME]
Processes all historical schedule files against YTD survey data
and generates a combined JSON file for import into tracking system.

HOW TO USE:
1. Make sure the YTD survey export is in this folder (set INPUT_FILE below)
2. Set SCHEDULES_DIR to the folder containing your schedule PDFs/Excel files
3. Run: python backfill_gc_history.py
4. Open output/full_history.json
5. In the tracking tab, import each week one at a time
   (paste the content of each week block into the import field)
"""

import os, json, sys
import openpyxl
from datetime import date, timedelta
from collections import defaultdict

# CONFIG
INPUT_FILE    = "SurveyExport-2026-05-31 Raw YTD.xlsx"
SCHEDULES_DIR = r"C:\path\to\schedules"
OUTPUT_DIR    = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

# Column indices (0-based) -- adjust per your export format
COL_DATE = 1; COL_METRIC_1 = 8; COL_METRIC_2 = 10; COL_METRIC_3 = 11
COL_SEGMENT = 211; COL_TARGET = 272

SCHEDULES_DIR_MOUNT = "/path/to/mounted/schedules"

def load_survey_data():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), INPUT_FILE)
    if not os.path.exists(path):
        path = "/path/to/mounted/SurveyExport/" + INPUT_FILE
    wb = openpyxl.load_workbook(path, read_only=True)
    rows = list(wb.active.iter_rows(values_only=True))
    return rows[1:]  # skip header

def has_value(v): return v not in (None, "", " ")

def is_4_or_5(v):
    try: return int(v) >= 4
    except: return False

def satisfaction_pct(scores):
    valid = [s for s in scores if has_value(s)]
    if not valid: return None
    return round(sum(1 for s in valid if is_4_or_5(s)) / len(valid) * 100, 1)

def overall_score(metric1, metric2, metric3):
    vals = [v for v in [metric1, metric2, metric3] if v is not None]
    return round(sum(vals) / len(vals), 1) if vals else None

def score_block(rows):
    m1 = satisfaction_pct([r[COL_METRIC_1] for r in rows])
    m2 = satisfaction_pct([r[COL_METRIC_2] for r in rows])
    m3 = satisfaction_pct([r[COL_METRIC_3] for r in rows])
    return overall_score(m1, m2, m3), m1, m2, m3, len(rows)

def get_target(data):
    for row in data:
        v = row[COL_TARGET]
        if has_value(v):
            try: return float(v)
            except: pass
    return 91.5

def filter_rows(data, start, end):
    out = []
    for row in data:
        d = row[COL_DATE]
        if not hasattr(d, 'date'): continue
        if start <= d.date() <= end:
            out.append(row)
    return out

def get_shift_owner(attribution, survey_date, segment_name):
    if hasattr(survey_date, 'date'): survey_date = survey_date.date()
    return attribution.get((survey_date, segment_name))

def load_schedule(filepath):
    """Load schedule from PDF or Excel, return attribution dict."""
    ext = filepath.lower().split('.')[-1]
    try:
        if ext in ('xlsx', 'xls'):
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from schedule_parser import parse_schedule
            return parse_schedule(filepath)
        else:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from pdf_schedule_parser import parse_pdf_schedule
            return parse_pdf_schedule(filepath)
    except Exception as e:
        print(f"    ERROR loading {os.path.basename(filepath)}: {e}")
        return None, {}

def attribution_week_range(attribution):
    """Get the min/max dates in the attribution dict."""
    dates = [d for d, seg in attribution.keys()]
    if not dates: return None, None
    return min(dates), max(dates)

def build_week_json(week_label, week_start, week_end, survey_data, attribution, target):
    """Build the JSON payload for one week."""
    week_rows = filter_rows(survey_data, week_start, week_end)
    if not week_rows:
        return None  # No surveys this week

    og, m1, m2, m3, n = score_block(week_rows)
    payload = {
        "week": week_label,
        "location": "[THEATER_NAME]",
        "target": target,
        "overall": {"score": og, "metric_1": m1, "metric_2": m2, "metric_3": m3, "surveys": n},
        "leaders": {}
    }

    # Attribute surveys to leaders
    leader_rows = defaultdict(list)
    for row in week_rows:
        d = row[COL_DATE]; seg = row[COL_SEGMENT]
        if not hasattr(d, 'date') or not seg: continue
        info = get_shift_owner(attribution, d.date(), seg)
        if not info: continue
        if info['mod']:
            leader_rows[info['mod'] + '|MOD'].append(row)
        for sup in info['supervisors']:
            leader_rows[sup + '|SUP'].append(row)

    for key, rows in leader_rows.items():
        name, role = key.rsplit('|', 1)
        l_og, l_m1, l_m2, l_m3, l_n = score_block(rows)
        payload['leaders'][name] = {
            'role': role,
            'score': l_og, 'metric_1': l_m1, 'metric_2': l_m2, 'metric_3': l_m3,
            'surveys': l_n
        }

    return payload

def main():
    print("\nSurvey History Backfill -- [THEATER_NAME]")
    print("=" * 45)

    # Load survey data
    survey_data = load_survey_data()
    target = get_target(survey_data)
    print(f"Survey data loaded: {len(survey_data)} responses, target={target}%")

    # Resolve schedules directory
    sched_dir = SCHEDULES_DIR if os.path.exists(SCHEDULES_DIR) else SCHEDULES_DIR_MOUNT
    if not os.path.exists(sched_dir):
        print(f"ERROR: Schedules directory not found: {sched_dir}")
        return

    sched_files = sorted([
        f for f in os.listdir(sched_dir)
        if f.lower().endswith(('.pdf', '.xlsx', '.xls'))
        and not f.startswith('.')
        and not f.startswith('~')
    ])
    print(f"Schedule files found: {len(sched_files)}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_weeks = []

    for fname in sched_files:
        fpath = os.path.join(sched_dir, fname)
        print(f"\nProcessing: {fname}")

        attribution, day_dates = load_schedule(fpath)
        if not attribution:
            print("    Skipped (no attribution data)")
            continue

        week_start, week_end = attribution_week_range(attribution)
        if not week_start:
            print("    Skipped (no dates found)")
            continue

        week_label = week_start.strftime("%b %d") + " - " + week_end.strftime("%b %d, %Y")
        print(f"    Week: {week_label}")

        payload = build_week_json(week_label, week_start, week_end, survey_data, attribution, target)

        if not payload:
            print(f"    No surveys found for this week — skipping")
            continue

        n = payload['overall']['surveys']
        og = payload['overall']['score']
        print(f"    Surveys: {n}  Overall Score: {og}%")
        print(f"    Leaders attributed: {list(payload['leaders'].keys())}")

        all_weeks.append(payload)

    # Sort by week descending (most recent first)
    all_weeks.sort(key=lambda w: w['week'], reverse=True)

    # Save individual week files
    for week in all_weeks:
        safe_name = week['week'].replace(' ', '_').replace(',', '').replace('-', 'to')
        with open(os.path.join(OUTPUT_DIR, f"week_{safe_name}.json"), 'w') as fh:
            json.dump(week, fh, indent=2)

    # Save combined file
    combined_path = os.path.join(OUTPUT_DIR, "full_history.json")
    with open(combined_path, 'w') as fh:
        json.dump(all_weeks, fh, indent=2)

    print(f"\n{'=' * 45}")
    print(f"Backfill complete: {len(all_weeks)} weeks processed")
    print(f"Combined file: {combined_path}")
    print(f"\nTO IMPORT INTO TRACKING SYSTEM:")
    print(f"  Open each week_*.json file in the output/ folder")
    print(f"  Paste the content into the tracking system import field")
    print(f"  Click Import Week — repeat for each week")
    print()

if __name__ == "__main__":
    main()
