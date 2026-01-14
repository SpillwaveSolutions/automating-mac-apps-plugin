---
name: meeting-start-agent
description: Detects the current meeting and starts a Voice Memo recording.
triggers:
  - pattern: "start meeting"
    type: keyword
  - pattern: "i am attending a meeting"
    type: keyword
skills:
  - automating-calendar
  - automating-voice-memos
  - automating-mac-apps
---

# Meeting Start Agent

Runs `meeting-start`: finds the in-progress meeting from Calendar and starts a Voice Memos recording named after it.
