---
name: automating-voice-memos
description: Automates Apple Voice Memos (Mac Catalyst, no dictionary) via JXA using filesystem/SQLite access and System Events UI scripting.
---

# Automating Voice Memos (no dictionary, data+UI hybrid)

## Relationship to the macOS automation skill
- This is a standalone skill for Voice Memos automation.
- For setup help, see the `automating-mac-apps` skill for permissions (Full Disk Access, Accessibility) and the ObjC bridge basics.
- Prerequisites: Basic JXA (JavaScript for Automation) knowledge; install via macOS System Preferences > Security & Privacy.

## Core Framing
- **Catalyst App**: Voice Memos is an iOS app adapted for macOS without full macOS APIs, hence no AppleScript dictionary for automation.
- **UI-first**: Prefer UI scripting/keyboard shortcuts for exports to avoid touching the database/container.
- **Data (optional)**: Use data-layer control only if needed (ObjC + sqlite3). This requires broader permissions.
- **Permissions**: Accessibility for UI automation; Full Disk Access only if you read/write the container/DB.

## Workflow (default)
1) UI-first (no FDA): export via menu/shortcut to a folder you control.
2) Optional data path: resolve storage paths; query CloudRecordings.db (Apple epoch +978307200) only if required.
3) For UI actions (recording/export), drive the app with System Events (shortcuts preferred over clicks).
4) For editing, prefer external tools (ffmpeg) after export; avoid writing directly into the container unless you accept FDA.

## Quickstart (UI-only export; no Full Disk Access)
- Open Voice Memos and select a recording.
- Export/share UI: the Share sheet can send audio to Notes/other apps (no direct File > Export).
- Transcript copy (UI-only, no FDA):
  - Run: `osascript skills/automating-voice-memos/scripts/copy_transcript_to_file.applescript "/path/to/output.txt"`
  - Defaults: Desktop/voice-memo-transcript.txt if no arg.
  - Shows transcript (if available), selects all, copies, and writes to the target file via clipboard.

## Permissions
- **Accessibility**: System Settings > Privacy & Security > Accessibility > Enable for System Events and your automation app (Terminal/Python/Script Editor).
- **Full Disk Access**: Only if you read/write the Voice Memos container/DB directly. UI-only exports do not require FDA.
- **Verify**: For UI-only, confirm you can open the Export menu and interact with the save dialog. For data access, verify `${home}/Library/Group Containers/group.com.apple.VoiceMemos.shared/`.

## Troubleshooting
- **Permission denied**: Verify Full Disk Access and Accessibility permissions.
- **Database locked**: Close Voice Memos app before querying.
- **File not found**: Check macOS version for correct storage path.
- **UI automation failures**: Ensure Voice Memos is focused and Accessibility is enabled.

## What to load
- Start with basics & prerequisites: `automating-voice-memos/references/voice-memos-basics.md` (setup and core concepts).
- UI automation: `automating-voice-memos/references/voice-memos-ui.md` (shortcuts, AX scripting).
- Data access (if needed): `automating-voice-memos/references/voice-memos-data.md` (storage paths, epochs, database schema).
- Recipes: `automating-voice-memos/references/voice-memos-recipes.md` (exports, transcripts, recording control).
