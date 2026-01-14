---
name: meeting-end
description: Stop the meeting Voice Memo, draft notes, and prepare follow-up email to attendees.
parameters:
  - name: memo-title
    description: Optional override for memo name to stop
    required: false
skills:
  - automating-voice-memos
  - automating-reminders
  - automating-mail
  - automating-calendar
  - automating-mac-apps
---

# Meeting End

Stops the active meeting recording, drafts meeting notes, and prepares a follow-up email to attendees.

## Usage
```
/meeting-end
/meeting-end --memo-title "Client Review"
```

## Behavior
1) Stops the active Voice Memos recording (matching the current meeting name unless overridden).  
2) Attempts to pull the Voice Memos transcript (if available) and uses it to draft structured meeting notes (agenda, decisions, action items).  
3) Prepares a draft email to attendees with notes and follow-ups for editing/sending (leveraging transcript when present).  
4) Optionally creates reminders for follow-up tasks extracted from the notes/transcript.  
5) (When `automating-notes` is available) files notes in Notes under `meetings/<company>/<date>-<meeting-title>` and can create/update people dossiers under `people/<first>-<last>/<date>-<title>` and `people/<first>-<last>/overview` (birthday, allergies, pets, family, etc.).  
