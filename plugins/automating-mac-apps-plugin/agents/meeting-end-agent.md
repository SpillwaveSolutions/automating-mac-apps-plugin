---
name: meeting-end-agent
description: Stops the active meeting recording, drafts notes, and prepares follow-up email/tasks.
triggers:
  - pattern: "meeting is over"
    type: keyword
  - pattern: "end meeting"
    type: keyword
skills:
  - automating-voice-memos
  - automating-reminders
  - automating-mail
  - automating-calendar
  - automating-mac-apps
---

# Meeting End Agent

Runs `meeting-end`: stops the meeting Voice Memo, pulls the transcript when available, drafts meeting notes, prepares a follow-up email to attendees, and can create reminders for action items. When the `automating-notes` skill is available, it can file meeting notes under `meetings/<company>/<date>-<meeting-title>` and update people dossiers under `people/<first>-<last>/...`.
