---
name: numbers-to-excel
description: Convert a Numbers document to Excel
parameters:
  - name: file
    description: Path to the .numbers file
    required: true
  - name: output
    description: Output .xlsx path (optional)
    required: false
  - name: sheet
    description: Sheet name to convert (optional)
    required: false
skills:
  - automating-numbers
  - automating-excel
  - automating-mac-apps
---

# Numbers to Excel

Converts a Numbers document to Excel format and preserves formatting where possible.

## Usage
```
/numbers-to-excel --file /path/to/input.numbers
/numbers-to-excel --file /path/to/input.numbers --output /path/to/output.xlsx
```

## Behavior
1) Opens Numbers and exports to an interchange format if needed.
2) Opens Excel and imports the data.
3) Saves to the output path if provided.
