---
name: meeting-setup-agent
description: Preps a meeting by syncing attendees to Contacts, creating prep reminders, and setting calendar alerts.
triggers:
  - pattern: "prepare for meeting"
    type: keyword
  - pattern: "set up meeting"
    type: keyword
  - pattern: "meeting prep"
    type: keyword
skills:
  - automating-contacts
  - automating-reminders
  - automating-calendar
  - automating-mac-apps
---

# Meeting Setup Agent

Runs `meeting-setup`: confirms attendees, upserts missing Contacts, creates prep reminders, and updates Calendar alerts (1 day/1 hour/15 minutes).
