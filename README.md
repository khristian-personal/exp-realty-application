# Python Scripts for Data Pipeline & Reporting

Four production-quality Python scripts demonstrating data integration, complex business logic, and automated reporting.

## Scripts

**SCRIPT_1_backfill_gc_history.py**  
Processes historical survey data against leadership schedules and generates weekly JSON payloads for system import.
```bash
python SCRIPT_1_backfill_gc_history.py
```

**SCRIPT_2_generate_gc_report.py**  
Analyzes survey data, calculates satisfaction metrics, tracks trends, and generates three formatted reports.
```bash
python SCRIPT_2_generate_gc_report.py
```

**SCRIPT_3_pdf_schedule_parser.py**  
Extracts leadership schedules from PDFs using coordinate-based text reconstruction.
```bash
python SCRIPT_3_pdf_schedule_parser.py path/to/schedule.pdf
```

**SCRIPT_4_schedule_parser.py**  
Extracts leadership schedules from Excel files with consistent output format.
```bash
python SCRIPT_4_schedule_parser.py path/to/schedule.xlsx
```

## Installation

```bash
pip install -r requirements.txt
```

## What They Do

- **Multi-source integration** — Combine Excel surveys + PDF/Excel schedules
- **Complex attribution** — Match survey responses to managers by date + time segment
- **Data aggregation** — Calculate scores, trends, and leader performance
- **Multiple output formats** — Generate JSON (system import), TXT (reports), and structured data

## Example Output

See `example_weekly_report.txt` and `example_weekly_data.json` for sample output.

## Key Skills Demonstrated

- Data pipeline design (ETL)
- File format parsing (Excel, PDF, JSON)
- Complex business logic
- Modular code architecture
- Error handling & graceful degradation
