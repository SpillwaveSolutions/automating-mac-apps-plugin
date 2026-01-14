---
name: csv-to-excel-agent
description: Imports CSV into Excel and applies formatting
triggers:
  - pattern: "csv to excel"
    type: keyword
  - pattern: ".csv"
    type: file_mention
  - pattern: "excel"
    type: keyword
skills:
  - automating-excel
  - automating-mac-apps
---

# CSV to Excel Agent

Handles CSV import and formatting in Excel.
