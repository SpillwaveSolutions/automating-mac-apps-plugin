---
name: sheet-report-agent
description: Analyzes spreadsheet data and produces a report with charts
triggers:
  - pattern: "report from spreadsheet"
    type: keyword
  - pattern: "sheet report"
    type: keyword
  - pattern: ".xlsx"
    type: file_mention
  - pattern: ".numbers"
    type: file_mention
  - pattern: "analyze spreadsheet"
    type: keyword
skills:
  - automating-numbers
  - automating-excel
  - automating-pages
  - automating-word
  - automating-keynote
  - automating-powerpoint
  - automating-mac-apps
---

# Sheet Report Agent

Analyzes a spreadsheet and generates a report with charts in Pages, Word, or Keynote.
