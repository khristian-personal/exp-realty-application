"""
Survey Score Automation -- [THEATER_NAME] (Unit [UNIT_ID])
Reads sanitized survey export, calculates satisfaction % scores, generates 3 outputs:
  1. crew_post.txt          -- Internal communication post
  2. leadership_email.txt   -- Leadership overview email
  3. shift_tracker.txt      -- Per-shift coaching reference

HOW TO USE:
1. Export raw data from survey system
2. Delete guest PII: name, email, address
3. Drop .xlsx into this folder, update INPUT_FILE below
4. Run: python generate_gc_report.py
5. Find outputs in output/

SCORING: Satisfaction% = % of surveys rating 4 or 5 out of 5
         Overall Score = average of Metric1%, Metric2%, Metric3%
"""

import openpyxl
from datetime import datetime, timedelta
from collections import defaultdict
import os

try:
    from schedule_parser import parse_schedule, get_shift_owner
    HAS_PARSER = True
except ImportError:
    HAS_PARSER = False

# CONFIG
INPUT_FILE     = "SurveyExport-2026-05-31 Raw YTD.xlsx"
SCHEDULE_FILE  = ""  # Optional: set to your weekly schedule .xlsx filename
THEATER    = "[THEATER_NAME]"
UNIT       = "[UNIT_ID]"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")

# Column indices (0-based) - adjust per your export
COL_DATE    = 1
COL_M1      = 8
COL_M2      = 10
COL_M3      = 11
COL_SEGMENT = 211
COL_CREW_YN = 37
COL_CREW_CM = 38
COL_TARGET  = 272

# Define which columns contain detailed feedback for each metric
METRIC_1_FEEDBACK = list(range(40, 54))
METRIC_2_FEEDBACK = list(range(54, 72))
METRIC_3_FEEDBACK = list(range(72, 80))

SEGMENT_ORDER = ["Morning","1st Shift","2nd Shift","3rd Shift",
                 "1st Evening","2nd Evening","3rd Evening"]
DOW_ORDER     = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


def load_data():
    path = os.path.join(SCRIPT_DIR, INPUT_FILE)
    if not os.path.exists(path):
        raise FileNotFoundError("Input file not found: " + path)
    wb = openpyxl.load_workbook(path, read_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    return rows[0], rows[1:]


def is_4_or_5(val):
    try: return int(val) >= 4
    except: return False

def has_value(val):
    return val not in (None, "", " ")

def satisfaction_pct(scores):
    valid = [s for s in scores if has_value(s)]
    if not valid: return None
    return round(sum(1 for s in valid if is_4_or_5(s)) / len(valid) * 100, 1)

def overall_score(m1_pct, m2_pct, m3_pct):
    vals = [v for v in [m1_pct, m2_pct, m3_pct] if v is not None]
    if not vals: return None
    return round(sum(vals) / len(vals), 1)

def week_range_for(dt):
    start = dt - timedelta(days=dt.weekday())
    return start.date(), (start + timedelta(days=6)).date()

def filter_rows(data, start_date, end_date):
    out = []
    for row in data:
        d = row[COL_DATE]
        if not hasattr(d, "date"): continue
        if start_date <= d.date() <= end_date:
            out.append(row)
    return out

def get_target(data):
    for row in data:
        v = row[COL_TARGET]
        if has_value(v):
            try: return float(v)
            except: pass
    return None

def score_block(rows):
    m1 = satisfaction_pct([r[COL_M1] for r in rows])
    m2 = satisfaction_pct([r[COL_M2] for r in rows])
    m3 = satisfaction_pct([r[COL_M3] for r in rows])
    return overall_score(m1, m2, m3), m1, m2, m3, len(rows)

def extract_crew_callouts(rows):
    out = []
    for row in rows:
        yn = str(row[COL_CREW_YN]).strip() if row[COL_CREW_YN] else ""
        cm = str(row[COL_CREW_CM]).strip() if row[COL_CREW_CM] else ""
        if yn in ("1","Y","Yes","YES","True","TRUE") and cm and len(cm) > 3:
            out.append(cm.replace("&nbsp;"," ").replace("&amp;","&").strip())
    return out

def extract_failure_points(rows, col_range):
    counts = defaultdict(int)
    noise = ["i dont usually","i don\x27t usually","no problem",
             "not a problem","everything was","nothing","n/a","na"]
    for row in rows:
        for col in col_range:
            if col < len(row) and has_value(row[col]):
                val = str(row[col]).strip()
                if val and val.lower() not in ("other","nan"):
                    if not any(n in val.lower() for n in noise):
                        counts[val] += 1
    return sorted(counts.items(), key=lambda x: -x[1])[:3]


def build_crew_post(week_scores, mtd_scores, target, callouts,
                    m3_fails, m1_fails, m2_fails, week_label):
    og, m1, m2, m3, n = week_scores
    mtd_og = mtd_scores[0]

    if target and og:
        diff = og - target
        if diff >= 2:
            headline = ("We're running " + str(round(diff,1)) + "pp ABOVE target this week. "
                       "That's not an accident -- that's you.")
        elif diff >= 0:
            headline = "Above target this week. Slim margin -- let's put some distance on it."
        elif diff >= -2:
            headline = ("We're " + str(round(abs(diff),1)) + "pp below target. "
                       "Close. Let's finish the week strong.")
        else:
            headline = ("We've got ground to make up. " + str(round(abs(diff),1)) +
                       "pp below target. It starts this shift.")
    else:
        headline = "Here's where we stand. Let's keep building."

    def indicator(val):
        if val is None: return ""
        if val >= 95: return " (excellent)"
        if val >= 91.5: return " (above target)"
        if val >= 88: return " (close)"
        return " (needs focus)"

    scores = {"Metric 1": m1, "Metric 2": m2, "Metric 3": m3}
    valid  = {k: v for k, v in scores.items() if v is not None}
    weakest   = min(valid, key=valid.get) if valid else None
    strongest = max(valid, key=valid.get) if valid else None

    lines = [
        "SURVEY RESULTS -- WEEK OF " + week_label.upper(),
        "[THEATER_NAME]  |  " + str(n) + " responses",
        "",
        "OVERALL: " + str(og) + "%" + indicator(og),
        "  Metric 1  " + str(m1) + "%" + indicator(m1),
        "  Metric 2  " + str(m2) + "%" + indicator(m2),
        "  Metric 3  " + str(m3) + "%" + indicator(m3),
        "",
        headline,
        "",
    ]

    if callouts:
        lines.append("RECOGNITION THIS WEEK:")
        for ct in callouts[:4]:
            short = ct[:130] + ("..." if len(ct) > 130 else "")
            lines.append('"' + short + '"')
        lines.append("")

    if weakest and valid[weakest] < 91.5:
        fails = {"Metric 1": m1_fails, "Metric 2": m2_fails, "Metric 3": m3_fails}[weakest]
        if fails:
            lines.append("THIS WEEK'S FOCUS -- " + weakest.upper() + ":")
            lines.append("Feedback: " + fails[0][0].lower() + ".")
            lines.append("That's our one thing to improve before next week.")
            lines.append("")
    elif strongest:
        lines.append("STANDOUT THIS WEEK: " + strongest + " at " + str(valid[strongest]) + "%.")
        lines.append("Name it out loud on shift. That's what excellence looks like.")
        lines.append("")

    lines.append("MTD we're at " + str(mtd_og) + "%. Target is " + str(target) + "%.")
    lines.append("Every shift moves the number. Make it count.")
    return "\n".join(lines)


def build_leadership_email(week_scores, prev_scores, mtd_scores, ytd_scores,
                           target, callouts, m3_fails, m1_fails, m2_fails,
                           week_label, shift_data, leader_summary=""):
    og,m1,m2,m3,n = week_scores
    p_og,p_m1,p_m2,p_m3,p_n = prev_scores if prev_scores else (None,)*5
    mtd_og,mtd_m1,mtd_m2,mtd_m3,mtd_n = mtd_scores
    ytd_og,ytd_m1,ytd_m2,ytd_m3,ytd_n = ytd_scores

    def fmt(val, prior=None):
        if val is None: return "N/A"
        s = str(val) + "%"
        if prior is not None:
            diff = val - prior
            s += " (" + ("+" if diff>=0 else "") + str(round(diff,1)) + "pp vs prior week)"
        return s

    lines = [
        "Subject: Survey Score Report -- " + week_label + " | [THEATER_NAME]",
        "",
        "SURVEY WEEKLY OVERVIEW -- [THEATER_NAME] (UNIT [UNIT_ID])",
        "Week of " + week_label + "  |  " + str(n) + " responses",
        "=" * 55,
        "",
        "THIS WEEK vs PRIOR WEEK:",
        "  Overall Score: " + fmt(og, p_og),
        "  Metric 1:      " + fmt(m1, p_m1),
        "  Metric 2:      " + fmt(m2, p_m2),
        "  Metric 3:      " + fmt(m3, p_m3),
        "",
        ("MTD (" + str(mtd_n) + " responses):  Overall " + str(mtd_og) + "%  |  "
         "M1 " + str(mtd_m1) + "%  |  M2 " + str(mtd_m2) + "%  |  M3 " + str(mtd_m3) + "%"),
        ("YTD (" + str(ytd_n) + " responses):  Overall " + str(ytd_og) + "%  |  "
         "M1 " + str(ytd_m1) + "%  |  M2 " + str(ytd_m2) + "%  |  M3 " + str(ytd_m3) + "%"),
        "Target: " + str(target) + "%",
        "",
    ]

    if shift_data:
        lines.append("SHIFT BREAKDOWN (this week):")
        lines.append("  " + "Day".ljust(12) + "Segment".ljust(16) +
                     "Score%".rjust(8) + "M1%".rjust(6) + "M2%".rjust(6) + "M3%".rjust(6) + "N".rjust(4))
        lines.append("  " + "-"*58)
        for (day,seg),(s_og,s_m1,s_m2,s_m3,s_n) in shift_data:
            def s(v): return (str(v)+"%").rjust(7) if v else "   N/A".rjust(7)
            lines.append("  " + day.ljust(12) + seg.ljust(16) +
                         s(s_og) + s(s_m1) + s(s_m2) + s(s_m3) + str(s_n).rjust(4))
        lines.append("")

    if m3_fails or m1_fails or m2_fails:
        lines.append("TOP FEEDBACK THEMES (this week):")
        for label, fails in [("Metric 1",m1_fails),("Metric 2",m2_fails),("Metric 3",m3_fails)]:
            if fails:
                lines.append("  " + label + ":")
                for item,cnt in fails:
                    lines.append("    - " + item + " (" + str(cnt) + "x)")
        lines.append("")

    if leader_summary:
        lines.append(leader_summary)
        lines.append("")

    if callouts:
        lines.append("RECOGNITION (" + str(len(callouts)) + " this week):")
        for ct in callouts:
            short = ct[:150] + ("..." if len(ct)>150 else "")
            lines.append('"' + short + '"')
        lines.append("")

    lines.append("-- Generated by [THEATER_NAME] Survey Automation")
    return "\n".join(lines)


def export_score_json(week_label, week_scores, leader_rows, target):
    """Export weekly data as JSON for tracking system import."""
    import json
    og, m1, m2, m3, n = week_scores
    payload = {
        "week": week_label,
        "location": "[THEATER_NAME]",
        "target": target,
        "overall": {"score": og, "metric_1": m1, "metric_2": m2, "metric_3": m3, "surveys": n},
        "leaders": {}
    }
    for leader_key, rows in leader_rows.items():
        l_og, l_m1, l_m2, l_m3, l_n = score_block(rows)
        role = "MOD" if "(MOD)" in leader_key else "SUP" if "(SUP)" in leader_key else "CL"
        name = leader_key.replace(" (MOD)","").replace(" (SUP)","").replace(" (CL)","").strip()
        payload["leaders"][name] = {
            "role": role,
            "score": l_og, "metric_1": l_m1, "metric_2": l_m2, "metric_3": l_m3,
            "surveys": l_n
        }
    return json.dumps(payload, indent=2)


def build_leader_summary(rows, attribution, target):
    """Attribute surveys to MOD/supervisor and calculate per-leader scores."""
    if not attribution:
        return ""

    leader_rows = defaultdict(list)
    unattributed = []

    for row in rows:
        d = row[COL_DATE]
        seg = row[COL_SEGMENT]
        if not hasattr(d, "date") or not seg:
            unattributed.append(row)
            continue
        info = get_shift_owner(attribution, d.date(), seg)
        if not info:
            unattributed.append(row)
            continue
        mod = info["mod"]
        sups = info["supervisors"]
        if mod:
            leader_rows[mod + " (MOD)"].append(row)
        for sup in sups:
            leader_rows[sup + " (SUP)"].append(row)
        if not mod and not sups:
            unattributed.append(row)

    if not leader_rows:
        return ""

    lines = ["LEADER CONTRIBUTION (this week):"]
    lines.append("  " + "Leader".ljust(28) + "Score%".rjust(8) + "M1%".rjust(7) +
                 "M2%".rjust(7) + "M3%".rjust(7) + "N".rjust(4) + "  vs Target")
    lines.append("  " + "-" * 68)

    for leader_key in sorted(leader_rows.keys()):
        l_rows = leader_rows[leader_key]
        og, m1, m2, m3, n = score_block(l_rows)
        def s(v): return (str(v) + "%").rjust(7) if v is not None else "   N/A".rjust(7)
        flag = ""
        if og and target:
            diff = og - target
            flag = ("+" + str(round(diff, 1)) + "pp") if diff >= 0 else (str(round(diff, 1)) + "pp")
        lines.append("  " + leader_key.ljust(28) +
                      s(og) + s(m1) + s(m2) + s(m3) + str(n).rjust(4) + "  " + flag)

    if unattributed:
        og, m1, m2, m3, n = score_block(unattributed)
        def s(v): return (str(v) + "%").rjust(7) if v is not None else "   N/A".rjust(7)
        lines.append("  " + "(no schedule match)".ljust(28) +
                      s(og) + s(m1) + s(m2) + s(m3) + str(n).rjust(4))
    return "\n".join(lines)


def build_shift_tracker(week_rows, week_label, attribution=None):
    by_shift = defaultdict(list)
    for row in week_rows:
        d = row[COL_DATE]
        seg = row[COL_SEGMENT] if row[COL_SEGMENT] else "Unknown"
        if hasattr(d,"strftime"):
            by_shift[(d.strftime("%A"), seg)].append(row)

    lines = [
        "SURVEY SHIFT TRACKER -- " + week_label.upper(),
        "[THEATER_NAME] | Unit [UNIT_ID]",
        "Use this for shift-level coaching conversations.",
        "",
        "Day".ljust(12) + "Segment".ljust(16) +
        "Score%".rjust(8) + "M1%".rjust(7) + "M2%".rjust(7) + "M3%".rjust(7) + "N".rjust(4) + "  Leader / Supervisor",
        "-"*85,
    ]

    tracker_data = []
    for day in DOW_ORDER:
        for seg in SEGMENT_ORDER:
            rows = by_shift.get((day,seg),[])
            if rows:
                s_og,s_m1,s_m2,s_m3,s_n = score_block(rows)
                tracker_data.append(((day,seg),(s_og,s_m1,s_m2,s_m3,s_n)))
                def s(v): return (str(v)+"%").rjust(7) if v else "   N/A".rjust(7)
                flag = ""
                if s_og and s_og < 90: flag = "<-- BELOW 90%"
                elif s_m3 and s_m3 < 88: flag = "<-- M3 LOW"
                elif s_m1 and s_m1 < 88: flag = "<-- M1 LOW"
                mod_info = ""
                if attribution:
                    from schedule_parser import get_shift_owner
                    from datetime import date as _date
                    for row in week_rows:
                        rd = row[COL_DATE]
                        if hasattr(rd, "strftime") and rd.strftime("%A") == day:
                            info = get_shift_owner(attribution, rd.date(), seg)
                            if info:
                                parts = []
                                if info["mod"]: parts.append(info["mod"].split()[0] + " (MOD)")
                                for sup in info["supervisors"]: parts.append(sup.split()[0] + " (SUP)")
                                mod_info = ", ".join(parts)
                            break
                if flag: mod_info = flag
                lines.append(day.ljust(12) + seg.ljust(16) +
                             s(s_og) + s(s_m1) + s(s_m2) + s(s_m3) + str(s_n).rjust(4) + "  " + mod_info)

    lines.append("")
    lines.append("Total surveys this week: " + str(len(week_rows)))
    lines.append("Flagged shifts are coaching priorities.")
    return "\n".join(lines), tracker_data


def main():
    print("\nSurvey Automation -- " + THEATER + " Unit " + UNIT)
    print("=" * 45)

    headers, data = load_data()
    target = get_target(data)
    today  = datetime.now().date()

    this_start, this_end = week_range_for(datetime.now())
    prev_start = this_start - timedelta(days=7)
    prev_end   = this_start - timedelta(days=1)
    month_start = today.replace(day=1)

    week_rows = filter_rows(data, this_start, this_end)
    prev_rows = filter_rows(data, prev_start, prev_end)
    mtd_rows  = filter_rows(data, month_start, today)
    ytd_rows  = data

    week_label = this_start.strftime("%b %d") + " - " + this_end.strftime("%b %d, %Y")
    report_rows  = week_rows if len(week_rows) >= 3 else mtd_rows
    report_label = week_label if len(week_rows) >= 3 else ("MTD (" + today.strftime("%B") + ")")

    print("Week: " + week_label + "  (" + str(len(week_rows)) + " responses)")
    print("MTD:  " + str(len(mtd_rows)) + " responses  |  YTD: " + str(len(ytd_rows)))

    week_scores = score_block(report_rows)
    prev_scores = score_block(prev_rows) if prev_rows else None
    mtd_scores  = score_block(mtd_rows)
    ytd_scores  = score_block(ytd_rows)

    og,m1,m2,m3,n = week_scores
    print("\nScores (" + report_label + "):")
    print("  Overall Score: " + str(og) + "%  (target: " + str(target) + "%)")
    print("  Metric 1: " + str(m1) + "%  |  Metric 2: " + str(m2) + "%  |  Metric 3: " + str(m3) + "%")

    # Load schedule for leader attribution (optional)
    attribution = None
    if SCHEDULE_FILE:
        import os as _os
        sched_path = _os.path.join(SCRIPT_DIR, SCHEDULE_FILE)
        if _os.path.exists(sched_path):
            try:
                if sched_path.endswith('.xlsx') or sched_path.endswith('.xls'):
                    from schedule_parser import parse_schedule as _parse
                else:
                    from pdf_schedule_parser import parse_pdf_schedule as _parse
                attribution, _ = _parse(sched_path)
                print("Schedule loaded: " + SCHEDULE_FILE)
            except Exception as e:
                print("Schedule load failed: " + str(e))

    callouts       = extract_crew_callouts(report_rows)
    m3_fails    = extract_failure_points(report_rows, METRIC_3_FEEDBACK)
    m1_fails = extract_failure_points(report_rows, METRIC_1_FEEDBACK)
    m2_fails    = extract_failure_points(report_rows, METRIC_2_FEEDBACK)

    tracker_text, tracker_data = build_shift_tracker(report_rows, report_label, attribution)
    crew_post  = build_crew_post(week_scores, mtd_scores, target,
                                 callouts, m3_fails, m1_fails, m2_fails, report_label)
    leader_summary = build_leader_summary(report_rows, attribution, target) if attribution else ""
    leadership = build_leadership_email(week_scores, prev_scores, mtd_scores, ytd_scores,
                                        target, callouts, m3_fails, m1_fails, m2_fails,
                                        report_label, tracker_data, leader_summary)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Build leader_rows for JSON export
    leader_rows_for_json = {}
    if attribution:
        for row in report_rows:
            d = row[COL_DATE]
            seg = row[COL_SEGMENT]
            if not hasattr(d, "date") or not seg: continue
            info = get_shift_owner(attribution, d.date(), seg)
            if not info: continue
            if info["mod"]:
                key = info["mod"] + " (MOD)"
                leader_rows_for_json.setdefault(key, []).append(row)
            for sup in info["supervisors"]:
                key = sup + " (SUP)"
                leader_rows_for_json.setdefault(key, []).append(row)

    score_json = export_score_json(report_label, week_scores, leader_rows_for_json, target)
    with open(os.path.join(OUTPUT_DIR,"weekly_data.json"),"w") as fh: fh.write(score_json)

    with open(os.path.join(OUTPUT_DIR,"crew_post.txt"),"w") as fh: fh.write(crew_post)
    with open(os.path.join(OUTPUT_DIR,"leadership_email.txt"),"w") as fh: fh.write(leadership)
    with open(os.path.join(OUTPUT_DIR,"shift_tracker.txt"),"w") as fh: fh.write(tracker_text)

    print("\nOutputs saved to " + OUTPUT_DIR)
    print("  weekly_data.json  <-- paste this into tracking system")
    print("  crew_post.txt")
    print("  leadership_email.txt")
    print("  shift_tracker.txt\n")


if __name__ == "__main__":
    main()
