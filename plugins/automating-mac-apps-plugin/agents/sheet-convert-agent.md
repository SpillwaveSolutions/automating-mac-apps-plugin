---
name: sheet-convert-agent
description: Converts between Excel and Numbers formats
triggers:
  - pattern: "excel to numbers"
    type: keyword
  - pattern: "numbers to excel"
    type: keyword
  - pattern: ".xlsx"
    type: file_mention
  - pattern: ".numbers"
    type: file_mention
  - pattern: "convert"
    type: keyword
skills:
  - automating-excel
  - automating-numbers
  - automating-mac-apps
---

# Sheet Convert Agent

Converts spreadsheets between Excel and Numbers.
