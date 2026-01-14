---
name: csv-to-numbers-agent
description: Imports CSV into Numbers and applies formatting
triggers:
  - pattern: "csv to numbers"
    type: keyword
  - pattern: ".csv"
    type: file_mention
  - pattern: "numbers"
    type: keyword
skills:
  - automating-numbers
  - automating-mac-apps
---

# CSV to Numbers Agent

Handles CSV import and formatting in Numbers.
