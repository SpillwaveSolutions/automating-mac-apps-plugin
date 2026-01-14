---
name: sheet-report
description: Analyze a Numbers or Excel file and generate a report with charts
parameters:
  - name: file
    description: Path to the spreadsheet (.numbers or .xlsx)
    required: true
  - name: output
    description: Output report path (Pages/Word/Keynote)
    required: false
  - name: format
    description: Report format: pages|word|keynote|powerpoint
    required: false
  - name: chart-types
    description: Comma-separated chart types (pie,bar,line)
    required: false
  - name: theme
    description: Template/theme name for the report (optional)
    required: false
skills:
  - automating-numbers
  - automating-excel
  - automating-pages
  - automating-word
  - automating-keynote
  - automating-powerpoint
  - automating-mac-apps
---

# Spreadsheet Report

Analyzes a spreadsheet and produces a report with charts. This command triggers the report agent for data analysis and report generation.

## Usage
```
/sheet-report --file /path/to/input.xlsx --format keynote
```

## Behavior
1) Loads the spreadsheet and profiles the data.
2) Creates charts (pie/line/bar) when appropriate.
3) Generates a report in Pages, Word, or Keynote.
