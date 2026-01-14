---
name: excel-to-numbers
description: Convert an Excel workbook to Numbers
parameters:
  - name: file
    description: Path to the .xlsx file
    required: true
  - name: output
    description: Output .numbers path (optional)
    required: false
  - name: sheet
    description: Sheet name to convert (optional)
    required: false
skills:
  - automating-excel
  - automating-numbers
  - automating-mac-apps
---

# Excel to Numbers

Converts an Excel workbook to Numbers format and preserves formatting where possible.

## Usage
```
/excel-to-numbers --file /path/to/input.xlsx
/excel-to-numbers --file /path/to/input.xlsx --output /path/to/output.numbers
```

## Behavior
1) Opens Excel and exports to an interchange format if needed.
2) Opens Numbers and imports the data.
3) Saves to the output path if provided.
