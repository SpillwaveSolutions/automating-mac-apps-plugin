# Automating Mac Apps Plugin

Automates macOS apps via Apple Events using AppleScript (discovery), JXA (legacy production logic), and PyXA/Python (preferred). Bundles per-app skills (Calendar, Notes, Mail, Keynote, Excel, Reminders, plus others) with quickstart scripts.

## Goals
- Fast discovery and prototyping for macOS app automation.
- Provide per-app recipes plus read-only “warm-up” scripts that trigger Automation prompts safely.
- Keep everything runnable from Terminal or by prompting Claude to run the setup scripts.

## Install
Clone into your Claude skills directory:

```bash
cd ~/.claude/skills
git clone https://github.com/SpillwaveSolutions/automating-mac-apps-plugin.git
```

## First-run setup (surface Automation prompts)
- Ask Claude to run: `skills/automating-mac-apps/scripts/request_automation_permissions.sh` (or `.py`) to trigger read-only checks for Calendar, Notes, Mail, Keynote, Excel, and Reminders. Run from the same host you’ll automate with (Terminal vs Python) so the correct app is approved.
- Or run per-app scripts (read-only):
  - `skills/automating-calendar/scripts/set_up_calendar_automation.{sh,py}`
  - `skills/automating-notes/scripts/set_up_notes_automation.{sh,py}`
  - `skills/automating-mail/scripts/set_up_mail_automation.{sh,py}`
  - `skills/automating-keynote/scripts/set_up_keynote_automation.{sh,py}`
  - `skills/automating-excel/scripts/set_up_excel_automation.{sh,py}`
  - `skills/automating-reminders/scripts/set_up_reminders_automation.{sh,py}`
  - Voice Memos (no AppleScript dictionary): `skills/automating-voice-memos/scripts/set_up_voice_memos_automation.sh` (activates app + checks data paths; enable Accessibility + consider Full Disk Access)
- Each script issues read-only AppleScript calls (list accounts/calendars/folders, etc.) and should prompt macOS to allow Terminal/Python control; click “Allow.”

## Structure
```
automating-mac-apps-plugin/
├── .claude-plugin/
│   └── marketplace.json
├── agents/
├── commands/
├── skills/
│   ├── automating-mac-apps/        # foundation + warm-up scripts
│   ├── automating-calendar/        # per-app skills (scripts folder inside)
│   ├── automating-notes/
│   ├── automating-mail/
│   ├── automating-keynote/
│   ├── automating-excel/
│   ├── automating-reminders/
│   └── ... (other app skills)
└── README.md
```

## License
MIT License - see LICENSE.
