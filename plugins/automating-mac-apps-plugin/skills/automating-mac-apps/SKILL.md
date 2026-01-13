---
name: automating-mac-apps
description: Automates macOS apps via Apple Events using AppleScript (discovery) and JXA (production logic). Use when asked about AppleScript, JXA, osascript, or macOS app automation.
---

# Automating macOS Apps (Apple Events, AppleScript, JXA)

## Core framing (use this mental model)
- Apple Events is the automation transport.
- AppleScript is the DSL for Apple Events: best for discovery, dictionaries, and quick prototypes.
- JXA (JavaScript for Automation) is a real programming language binding to the same Apple Events layer: best for data handling, JSON, and maintainable logic.
- Both have identical automation reach; differences are ergonomics, tooling, and maintainability.

## When to use which
- Use **AppleScript** for discovery, dictionary exploration, UI scripting, and quick one-offs.
- Use **JXA** for robust logic, JSON pipelines, integration with Python/Node, and long-lived automation.
- Hybrid pattern (recommended): discover in AppleScript, implement in JXA for production use.

## Workflow (default)
1) **Identify target app + dictionary** using Script Editor.
2) **Prototype** a minimal command that works.
3) **Decide language** using the rules above.
4) **Harden**: add error handling, timeouts, and permission checks.
5) **Validate**: run a read-only command and check outputs.
6) **Integrate** via `osascript` for CLI or pipeline use.
7) **UI scripting fallback** only when the dictionary is missing/incomplete.

## Reliability checklist
- Verify Automation permissions (System Settings > Privacy & Security > Automation).
- Verify Accessibility permissions for UI scripting.
- Prefer dictionary commands over UI scripting.
- Add waits/retries around UI operations.
- Keep scripts idempotent; check state before acting.

## When not to use this skill
- Cross-platform automation without Apple Events.
- Full UI testing (use XCTest or dedicated UI test tools).
- Environments that block Automation or Accessibility permissions.

## What to load
- For AppleScript syntax + patterns: `automating-mac-apps/references/applescript-basics.md`
- For AppleScript developer guide (condensed): `automating-mac-apps/references/applescript-guide.md`
- For AppleScript ASObjC helpers: `automating-mac-apps/references/applescript-asobjc.md`
- For AppleScript performance patterns: `automating-mac-apps/references/applescript-performance.md`
- For AppleScript timeouts and async patterns: `automating-mac-apps/references/applescript-timeouts.md`
- For JXA syntax + patterns + ObjC bridge: `automating-mac-apps/references/jxa-basics.md`
- For JXA cookbook (condensed): `automating-mac-apps/references/jxa-cookbook.md`
- For side-by-side recipes, pipelines, and helper library: `automating-mac-apps/references/recipes.md`
- For AppleScript -> JXA translation: `automating-mac-apps/references/translation-checklist.md`
- For reusable JXA helpers: `automating-mac-apps/references/jxa-helpers.js`
- For app-specific JXA recipes: `automating-mac-apps/references/jxa-mail.md`, `automating-mac-apps/references/jxa-finder.md`, `automating-mac-apps/references/jxa-pages.md`, `automating-mac-apps/references/jxa-safari.md`, `automating-mac-apps/references/jxa-chrome.md`, `automating-mac-apps/references/jxa-keynote.md`, `automating-mac-apps/references/jxa-calendar-notes.md`
- For CI/CD and TCC constraints: `automating-mac-apps/references/ci-cd-tcc.md`
- For shell environment pitfalls: `automating-mac-apps/references/shell-environment.md`
- For UI scripting inspection tips: `automating-mac-apps/references/ui-scripting-inspector.md`
- For VS Code workflow: `automating-mac-apps/references/tooling-vscode.md`
- For dictionary exploration: `automating-mac-apps/references/dictionary-strategies.md`
- For `whose` batching patterns: `automating-mac-apps/references/whos-batching.md`
- For security prompts and Automation permissions: `automating-mac-apps/references/security-prompts.md`

## Output expectations
- Keep examples minimal and runnable.
- Favor `osascript`-friendly output (stdout, JSON when in JXA).
- Explain where the app dictionary is used and why.
