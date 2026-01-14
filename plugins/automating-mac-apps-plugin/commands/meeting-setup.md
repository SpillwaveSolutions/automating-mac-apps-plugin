---
name: meeting-setup
description: Prepare for a meeting by syncing attendees to Contacts, creating prep reminders, and updating Calendar alerts.
parameters:
  - name: title
    description: Meeting title
    required: true
  - name: start
    description: ISO start datetime (e.g., 2024-07-01T15:00)
    required: true
  - name: end
    description: ISO end datetime (optional)
    required: false
  - name: attendees
    description: Comma-separated attendee emails/names
    required: true
  - name: prep-tasks
    description: Comma-separated prep tasks (default: create slide deck, write proposal)
    required: false
skills:
  - automating-contacts
  - automating-reminders
  - automating-calendar
  - automating-mac-apps
---

# Meeting Setup

Prepares a meeting by ensuring attendees exist in Contacts, creating prep reminders, and setting calendar alerts.

## Usage
```
/meeting-setup --title "Client Review" --start 2024-07-01T15:00 \
  --end 2024-07-01T16:00 \
  --attendees "alice@example.com, Bob <bob@example.com>" \
  --prep-tasks "create slide deck, write proposal, gather metrics"
```

## Behavior
1) Parses attendees; checks Contacts and offers to upsert missing people.  
2) Creates prep reminders (defaults: create slide deck, write proposal) in a prep list with due dates before the meeting.  
3) Updates/creates the Calendar event and sets alerts 1 day, 1 hour, and 15 minutes before.  
4) Confirms ready-state for follow-on commands (`meeting-start`, `meeting-end`), and notes that transcripts/notes will be harvested after the meeting for follow-ups.  
