---
name: csv-to-numbers
description: Convert a CSV into a formatted Numbers workbook
parameters:
  - name: file
    description: Path to the CSV file
    required: true
  - name: output
    description: Output .numbers path (optional)
    required: false
  - name: sheet
    description: Target sheet name (optional)
    required: false
  - name: table
    description: Target table name (optional)
    required: false
  - name: header-row
    description: Treat first row as header (true|false)
    required: false
  - name: theme
    description: Numbers template or theme name (optional)
    required: false
skills:
  - automating-numbers
  - automating-mac-apps
---

# CSV to Numbers

Converts a CSV into a formatted Numbers document. This command triggers the Numbers import agent for reliable, UI-aware formatting.

## Usage
```
/csv-to-numbers --file /path/to/input.csv
/csv-to-numbers --file /path/to/input.csv --output /path/to/output.numbers
```

## Behavior
1) Opens Numbers and imports the CSV.
2) Applies basic formatting (headers, column widths, number formats).
3) Saves to the output path if provided.
