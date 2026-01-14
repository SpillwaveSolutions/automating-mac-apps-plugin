---
name: meeting-start
description: Detect the current meeting, start a Voice Memo recording, and mark attendance.
parameters:
  - name: now
    description: Optional override datetime to pick the meeting (ISO)
    required: false
skills:
  - automating-calendar
  - automating-voice-memos
  - automating-mac-apps
---

# Meeting Start

Finds the in-progress meeting from Calendar and starts a Voice Memos recording for it.

## Usage
```
/meeting-start
/meeting-start --now 2024-07-01T15:05
```

## Behavior
1) Looks up the current (or provided) time in Calendar to identify the meeting.  
2) Activates Voice Memos and starts recording, naming the memo after the meeting.  
3) Optionally notes attendance/state for follow-up (`meeting-end`) and reminds that transcript/notes will be used downstream for action items.  
