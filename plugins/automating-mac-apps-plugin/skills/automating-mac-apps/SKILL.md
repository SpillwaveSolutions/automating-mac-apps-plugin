---
name: automating-mac-apps
description: Automates macOS apps via Apple Events using AppleScript (discovery) and JXA (production logic). Use when asked about AppleScript, JXA, osascript, or macOS app automation.
---

# Automating macOS Apps (Apple Events, AppleScript, JXA)

## ⚠️ Legacy Technology Notice

**Important**: JXA (JavaScript for Automation) and AppleScript are legacy automation technologies. They received their last major updates in 2015-2016 and are not actively maintained by Apple. While still functional, they may have compatibility issues with modern macOS versions, especially macOS Sequoia 15+.

**Recommended Modern Alternatives**:
- **Shortcuts App**: Apple's primary automation tool with visual workflow builder
- **Swift/Objective-C**: For high-performance, production-ready automation
- **Third-party tools**: Depending on use case (Puppeteer for web, native APIs for specific apps)

## macOS Sequoia 15 Compatibility Notes

Scripts developed for earlier macOS versions may fail in Sequoia 15 due to:
- Stricter TCC (Transparency, Consent, and Control) permissions
- Enhanced security restrictions on Apple Events
- Changes to AppleScript execution timeouts
- Sandboxing improvements affecting script persistence

**Testing Recommendation**: Always test automation scripts on target macOS versions before deployment.

## Core framing (use this mental model)
- **Apple Events**: The underlying inter-process communication (IPC) transport for macOS automation.
- **AppleScript**: The original DSL (Domain-Specific Language) for Apple Events: best for discovery, dictionaries, and quick prototypes.
- **JXA (JavaScript for Automation)**: A JavaScript binding to the Apple Events layer: best for data handling, JSON, and maintainable logic.
- **ObjC Bridge**: JavaScript access to Objective-C frameworks (Foundation, AppKit) for advanced macOS capabilities beyond app dictionaries.

## When to use which
- Use **AppleScript** for discovery, dictionary exploration, UI scripting, and quick one-offs.
- Use **JXA** for robust logic, JSON pipelines, integration with Python/Node, and long-lived automation.
- Hybrid pattern (recommended): discover in AppleScript, implement in JXA for production use.

## When to use this skill
- Foundation for app-specific skills (Calendar, Notes, Mail, Keynote, Excel, Reminders).
- Run the automation warm-up scripts before first automation to surface macOS permission prompts.
- Use as the base reference for permissions, shell integration, and UI scripting fallbacks.

## Workflow (default)
1) **Identify target app + dictionary** using Script Editor.
2) **Prototype** a minimal command that works.
   - *Example*: `tell application "Finder" to get name of first item in desktop`
3) **Decide language** using the rules above.
4) **Harden**: add error handling, timeouts, and permission checks.
   - *JXA*: `try { ... } catch (e) { console.log('Error:', e.message); }`
   - *AppleScript*: `try ... on error errMsg ... end try`
5) **Validate**: run a read-only command and check outputs.
   - *Example*: `osascript -e 'tell application "Finder" to get name of home'`
   - Confirm: Output matches expected (e.g., user home folder name)
6) **Integrate** via `osascript` for CLI or pipeline use.
7) **UI scripting fallback** only when the dictionary is missing/incomplete.
   - *Example UI Script*: `tell application "System Events" to click button 1 of window 1 of process "App"`
   - *Example JXA*: `Application('System Events').processes.byName('App').windows[0].buttons[0].click()`

## Reliability checklist (Prioritized)
1. **Permissions**: Verify Automation/Accessibility permissions (System Settings > Privacy & Security).
2. **State Check**: Ensure app is running (`Application("App").running()`).
3. **Idempotency**: Check state before acting (e.g., does folder exist?).
4. **Dictionary First**: Prefer direct object model over UI scripting.
5. **Waits**: Add delays/retries around UI operations.

## Automation permission warm-up
- Use before first automation run or after macOS updates to surface prompts:
  - All apps at once: `skills/automating-mac-apps/scripts/request_automation_permissions.sh` (or `.py`).
  - Per-app: `skills/automating-<app>/scripts/set_up_<app>_automation.{sh,py}` (calendar, notes, mail, keynote, excel, reminders).
  - Voice Memos (no dictionary): `skills/automating-voice-memos/scripts/set_up_voice_memos_automation.sh` to activate app + check data paths; enable Accessibility + consider Full Disk Access.
- Run from the same host you intend to automate with (Terminal vs Python) so the correct app gets Automation approval.
- Each script runs read-only AppleScript calls (list accounts/calendars/folders, etc.) to request Terminal/Python control; click “Allow” when prompted.

## Modern Python Alternatives to JXA

**PyXA (Python for macOS Automation)** - **Strongly Recommended** over JXA for new projects:

### Why PyXA Is Preferred
- **Active Development**: Regularly maintained with updates (latest v0.2.3 as of 2026)
- **Modern Python Syntax**: Clean, readable code with standard Python conventions
- **Rich Feature Set**: Beyond JXA capabilities - UI scripting, clipboard, notifications, speech recognition
- **Better Documentation**: Extensive examples, tutorials, active Discord community
- **Command Chaining**: Intuitive method chaining like `app.lists().reminders().title()`

### PyXA Capabilities
- **App Automation**: Safari, Calendar, Reminders, Mail, Music, and more
- **UI Scripting**: Access to non-scriptable apps via UI elements
- **System Integration**: Notifications, dialogs, clipboard, sound processing
- **AppleScript Integration**: Can load and execute AppleScript from Python

### PyXA Installation {#pyxa-installation}

```bash
# Install PyXA
pip install mac-pyxa

# Or with pip3 explicitly
pip3 install mac-pyxa

# Requirements:
# - Python 3.10+ (check with: python3 --version)
# - macOS 12+ (Monterey or later recommended)
# - PyObjC is installed automatically as a dependency

# Verify installation
python3 -c "import PyXA; print(f'PyXA {PyXA.__version__} installed successfully')"
```

> **Note:** All app-specific skills in this plugin that show PyXA examples assume PyXA is installed. See this section for installation.

### PyXA Example (Safari Automation)
```python
import PyXA

# Launch Safari and navigate
safari = PyXA.Safari()
safari.activate()
safari.open_location("https://example.com")

# Get current tab URL
current_url = safari.current_tab.url
print(f"Current URL: {current_url}")
```

### PyXA Example (Reminders)
```python
import PyXA

reminders = PyXA.Reminders()
work_list = reminders.lists().by_name("Work")

# Add new reminder
new_reminder = work_list.reminders().push({
    "name": "Review PyXA documentation",
    "body": "Explore modern macOS automation options"
})
```

**PyXA Official Resources**:
- Documentation: https://skaplanofficial.github.io/PyXA/
- GitHub: https://github.com/SKaplanOfficial/PyXA
- Community: Active Discord and GitHub discussions

---

**PyObjC (Python-Objective-C Bridge)** - For Low-Level macOS Integration:

### PyObjC Capabilities
- **Direct Framework Access**: AppKit, Foundation, and all macOS frameworks
- **Apple Events**: Send Apple Events via Scripting Bridge
- **Script Execution**: Run AppleScript or JXA from Python
- **System APIs**: Direct access to CalendarStore, AddressBook, SystemEvents

### Installation
```bash
pip install pyobjc
# Installs bridges for major frameworks
```

### PyObjC Example (AppleScript Execution)
```python
from Foundation import NSAppleScript

# Execute AppleScript from Python
script_source = '''
tell application "Safari"
    return URL of current tab
end tell
'''

script = NSAppleScript.alloc().initWithSource_(script_source)
result, error = script.executeAndReturnError_(None)

if error:
    print(f"Error: {error}")
else:
    print(f"Current Safari URL: {result.stringValue()}")
```

### PyObjC Example (App Control via Scripting Bridge)
```python
from ScriptingBridge import SBApplication

# Control Mail app
mail = SBApplication.applicationWithBundleIdentifier_("com.apple.Mail")
inbox = mail.inboxes()[0]  # Access first inbox

# Get unread message count
unread_count = inbox.unreadCount()
print(f"Unread messages: {unread_count}")
```

**PyObjC Official Resources**:
- Documentation: https://pyobjc.readthedocs.io
- Examples: Extensive GitHub repositories with code samples

---

### JXA Status and Migration
**JXA (JavaScript for Automation)** is **effectively abandoned**:
- No updates since 2016
- Fragile and inconsistent behavior
- Poor error handling and debugging
- Limited community support

**Migration Recommendation**: Use PyXA for most automation needs. It's more reliable, better documented, and actively maintained.

## When not to use this skill
- Cross-platform automation (use Selenium/Playwright for web, Python for generic tasks).
- Full UI testing (use XCUITest or Appium).
- Environments that strictly block Automation or Accessibility permissions.
- **New projects**: Consider PyXA or PyObjC instead of JXA.

## Related Skills
- App-specific automation (create `automating-[app]` skills as needed)
- `ci-cd-tcc` for advanced permission management in automated environments
- `mastering-applescript` for AppleScript-focused workflows

## Security Best Practices

**Permission Management**:
- Request minimal required permissions to reduce security risks
- Use code signing for production scripts (Developer ID certificate)
- Store credentials securely (Keychain, not hardcoded)
- Validate all inputs to prevent injection attacks

**Official Apple Security Guidance**:
- [Apple Platform Security Guide](https://support.apple.com/guide/security/welcome/web)
- [Scripting security considerations](https://support.apple.com/guide/security/secf202c9f70/web)
- [App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html)

## Output expectations
- Keep examples minimal and runnable.
- **JSON Output**: For CLI pipelines, use `JSON.stringify(result)` in JXA.
  - *Example*: `console.log(JSON.stringify({files: files, count: files.length}))`
- **Exit Codes**: Ensure `osascript` exits with 0 for success, non-zero for failure.

## What to load

### Tier 1: Essentials (Start Here)
- JXA Syntax & Patterns: `automating-mac-apps/references/basics.md`
- AppleScript Basics: `automating-mac-apps/references/applescript-basics.md`
- Cookbook (Common Recipes): `automating-mac-apps/references/recipes.md`

### Tier 2: Advanced & Production
- JXA Cookbook (Condensed): `automating-mac-apps/references/cookbook.md`
- Performance Patterns: `automating-mac-apps/references/applescript-performance.md`
- CI/CD & Permissions: `automating-mac-apps/references/ci-cd-tcc.md`
- Shell Environment: `automating-mac-apps/references/shell-environment.md`
- UI Scripting Inspector: `automating-mac-apps/references/ui-scripting-inspector.md`

### Tier 3: Specialized & Reference
- **PyXA Core API Reference** (complete class/method docs): `automating-mac-apps/references/pyxa-core-api-reference.md`
- PyXA Basics: `automating-mac-apps/references/pyxa-basics.md` (Modern Python automation fundamentals)
- AppleScript → PyXA Conversion: `automating-mac-apps/references/applescript-to-pyxa-conversion.md` (Migration guide with examples)
- Translation Checklist (AppleScript → JXA): `automating-mac-apps/references/translation-checklist.md` (Comprehensive guide with examples and pitfalls)
- JXA Helpers Library: `automating-mac-apps/references/helpers.js`
- `whose` Batching Patterns: `automating-mac-apps/references/whos-batching.md`
- Dictionary Strategies: `automating-mac-apps/references/dictionary-strategies.md`
- ASObjC Helpers: `automating-mac-apps/references/applescript-asobjc.md`

**Related Skills**:
- `web-browser-automation`: Complete browser automation guide (Chrome, Edge, Brave, Arc)
