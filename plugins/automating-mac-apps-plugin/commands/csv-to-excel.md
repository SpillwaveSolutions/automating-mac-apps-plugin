---
name: csv-to-excel
description: Convert a CSV into a formatted Excel workbook
parameters:
  - name: file
    description: Path to the CSV file
    required: true
  - name: output
    description: Output .xlsx path (optional)
    required: false
  - name: sheet
    description: Target sheet name (optional)
    required: false
  - name: header-row
    description: Treat first row as header (true|false)
    required: false
  - name: theme
    description: Excel template name (optional)
    required: false
skills:
  - automating-excel
  - automating-mac-apps
---

# CSV to Excel

Converts a CSV into a formatted Excel document. This command triggers the Excel import agent for reliable formatting.

## Usage
```
/csv-to-excel --file /path/to/input.csv
/csv-to-excel --file /path/to/input.csv --output /path/to/output.xlsx
```

## Behavior
1) Opens Excel and imports the CSV.
2) Applies basic formatting (headers, column widths, number formats).
3) Saves to the output path if provided.
