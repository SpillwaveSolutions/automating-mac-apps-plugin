---
name: automating-messages
description: Automates macOS Messages (iMessage/SMS) via JXA with reliable service→buddy resolution, send-bug workarounds, UI scripting for attachments, chat.db forensics, and launchd polling bots. Use when sending/managing Messages via automation, reading history with SQL, or building resilience around the flaky JXA bridge.
---

# Automating Messages (JXA-first with UI/DB fallbacks)

## Permissions and scope
- Grants needed: Automation + Accessibility; Full Disk Access for any `chat.db` reads.
- Keep automation scoped and auditable; avoid unsolicited sends and DB writes.
- Pairs with `automating-mac-apps` for common setup (permissions, osascript invocation, UI scripting basics).

## Default workflow (happy path)
1) **Resolve transport**: pick `serviceType` (`iMessage` or `SMS`) before targeting a buddy.
2) **Identify recipient**: filter buddies by `handle` (phone/email). Avoid ambiguous names.
3) **Send via app-level `send`**: pass the Buddy object to `Messages.send()` (bridges around the JXA bug).
4) **Verify window context**: activate Messages when mixing with UI steps; avoid long `chat.messages()` reads.
5) **Fallbacks**: if send/attachments fail, switch to UI scripting; if reading history is needed, use SQL.

## Quick recipe (defensive send)
```javascript
const Messages = Application('Messages');
Messages.includeStandardAdditions = true;

function safeSend(text, handle, svcType = 'iMessage') {
  const svc = Messages.services.whose({ serviceType: svcType })[0];
  if (!svc) throw new Error(`Service ${svcType} missing`);
  const buddy = svc.buddies.whose({ handle })[0];
  if (!buddy) throw new Error(`Buddy ${handle} missing on ${svcType}`);
  Messages.send(text, { to: buddy });
}
```
- Wrap with `try/catch` and log; add small delays when activating UI.
- For groups, target an existing chat by GUID or fall back to UI scripting; array sends are unreliable.

## Attachments and UI fallback
- Messages lacks a stable JXA attachment API; use clipboard + System Events paste/send.
- Ensure Accessibility permission, bring app forward, paste file, press Enter.
- See `references/ui-scripting-attachments.md` for the full flow and ObjC pasteboard snippet.

## Data access and forensics
- Use SQL against `chat.db` for history; `chat.messages()` is slow and often redacted.
- Remember Cocoa epoch conversion; use `sqlite3 -json` for structured results.
- See `references/database-forensics.md` for schema notes, typedstream handling, and export tooling.

## Bots and monitoring
- Implement polling daemons with `launchd` now that on-receive handlers are gone.
- Track `rowid`, query diffs, dispatch actions, and persist state.
- See `references/monitoring-daemons.md` for the polling pattern and plist notes.

## What to load
- Control plane and send reliability: `references/control-plane.md`
- UI scripting + attachments fallback: `references/ui-scripting-attachments.md`
- SQL/history access: `references/database-forensics.md`
- Polling bots/launchd: `references/monitoring-daemons.md`
