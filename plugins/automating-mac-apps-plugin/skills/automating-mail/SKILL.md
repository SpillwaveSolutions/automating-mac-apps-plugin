---
name: automating-mail
description: Automates Apple Mail via JXA with AppleScript dictionary discovery. Covers accounts, mailboxes, batch message filtering, composition, attachments, and UI fallback.
---

# Automating Apple Mail (JXA-first, AppleScript discovery)

## ⚠️ Security Warning

**Important**: Mail automation involves sensitive email data and can be abused for malicious purposes. AppleScript has been used in malware campaigns. Always:
- Use code signing for production scripts
- Request minimal permissions only
- Validate all inputs to prevent injection attacks
- Only run scripts from trusted sources

**Modern Alternatives**:
- **Shortcuts App**: Visual automation with better security controls
- **Mail plugins**: Third-party tools like Canary Mail or Spark with built-in automation
- **API-based solutions**: For cross-platform email automation

## Prerequisites and Overview
- **JXA (JavaScript for Automation)**: Apple's JavaScript-based scripting framework for macOS apps, allowing JavaScript syntax with native app integration.
- **AppleScript**: macOS's native scripting language for app automation.
- **When to use**: Choose JXA for complex logic/data handling; AppleScript for simple commands.
- **Requirements**: macOS 10.10+, Script Editor app.

## Relationship to the macOS automation skill
- **Integration with `automating-mac-apps`**: Use this skill for Mail-specific automation. Reference `automating-mac-apps` for:
  - Permission setup (System Preferences > Security & Privacy > Automation)
  - Shell command integration (e.g., `osascript` for AppleScript execution)
  - UI scripting fallbacks (when Mail dictionary lacks functionality)
- **Complementary usage**: Load `automating-mac-apps` first for foundation, then this skill for Mail operations.

## Security Considerations

**Permission Requirements**:
- Mail automation requires extensive permissions that can be risky
- Grant access in System Settings → Privacy & Security → Automation
- Consider using dedicated automation tools instead of direct Mail scripting

**Best Practices**:
- Never hardcode credentials in scripts
- Use secure credential storage (Keychain)
- Implement proper error handling to avoid data exposure
- Test scripts in isolated environments first

**Official Apple Guidance**:
- [Mail automation security](https://support.apple.com/guide/mail/automate-tasks-mlhlp1013/mac)
- [Scripting security considerations](https://support.apple.com/guide/security/secf202c9f70/web)

## Core Framing
- Mail dictionary is AppleScript-first; discover there.
- **ObjC bridge**: Direct access to macOS Objective-C frameworks from JXA for advanced functionality (e.g. file system).
- **Objects are specifiers**: Mail objects (messages, mailboxes) are represented as dynamic references; read properties via method calls (e.g., `message.subject()`), modify via assignments (e.g., `message.readStatus = true`).

## Workflow (default)
0) **Prerequisites**: Ensure Mail app is configured, enable automation permissions.
1) Discover terms in Script Editor (Mail dictionary).
2) Prototype minimal AppleScript commands.
3) Port to JXA and add defensive checks.
4) Use batch reads (message properties on collections).
5) Use UI scripting for signature and UI-only actions.

## Quick Start Examples

**Prototype (AppleScript):**
```applescript
tell application "Mail"
    get subject of first message of inbox
end tell
```

**Production (JXA - Legacy):**
```javascript
const Mail = Application('Mail');
const message = Mail.inbox.messages[0];
console.log(message.subject());
```

**PyXA (Recommended Modern Approach):**
```python
import PyXA

mail = PyXA.Mail()

# Get first inbox message
inbox = mail.inboxes()[0]
message = inbox.messages()[0]
print(f"Subject: {message.subject()}")
print(f"Sender: {message.sender()}")
print(f"Date: {message.date_sent()}")
```

**PyObjC with Scripting Bridge:**
```python
from ScriptingBridge import SBApplication

mail = SBApplication.applicationWithBundleIdentifier_("com.apple.Mail")

# Access inbox messages
inbox = mail.inboxes()[0]
messages = inbox.messages()

if messages:
    first_message = messages[0]
    print(f"Subject: {first_message.subject()}")
    print(f"Sender: {first_message.sender()}")
```

**Composition (JXA - Legacy):**
```javascript
const msg = Mail.OutgoingMessage({
  subject: "Status Update",
  content: "All systems go."
});
Mail.outgoingMessages.push(msg);
msg.visible = true;
```

**Composition (PyXA - Recommended):**
```python
import PyXA

mail = PyXA.Mail()

# Create new message
message = mail.outgoing_messages().push({
    "subject": "Status Update",
    "content": "All systems go.",
    "to_recipients": ["recipient@example.com"]
})

# Make visible to edit/send
message.visible = True
```

## Troubleshooting
- **Permission errors**: Check Automation permissions in System Preferences > Security & Privacy.
- **Dictionary access fails**: Use Script Editor > File > Open Dictionary > Mail to verify terms.
- **UI scripting needed**: For actions not in dictionary (e.g., signatures), use `System Events` app with `UI elements`.
- **Common JXA errors**: `message.subject is not a function` → Use `message.subject()` for reads.

## What to load
- Mail JXA basics: `automating-mail/references/mail-basics.md`
- Recipes (filter, move, compose): `automating-mail/references/mail-recipes.md`
- Advanced patterns (batch ops, HTML, signatures): `automating-mail/references/mail-advanced.md`
- Dictionary translation table: `automating-mail/references/mail-dictionary.md`
- Rule scripts: `automating-mail/references/mail-rules.md`
- HTML + signature workflow: `automating-mail/references/html-signature-workflow.md`
- Attachment extraction pipeline: `automating-mail/references/attachment-extraction.md`
- Mailbox archiver: `automating-mail/references/mailbox-archiver.md`
- HTML data merge: `automating-mail/references/html-data-merge.md`
- **PyXA API Reference** (complete class/method docs): `automating-mail/references/mail-pyxa-api-reference.md`