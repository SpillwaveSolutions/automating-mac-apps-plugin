---
name: automating-pages
description: Automates Apple Pages using JXA with AppleScript dictionary discovery. Covers documents, templates, text, styles, export, tables, images, and AppleScript bridge fallbacks. Prerequisites: Basic JXA knowledge and macOS automation experience. Target: Developers automating Pages documents via code.
---

# Automating Pages (JXA-first, AppleScript discovery)

## Relationship to the macOS automation skill
- Standalone for Pages, aligned with `automating-mac-apps` patterns.
- Use `automating-mac-apps` for permissions, shell, and UI scripting guidance.
- **PyXA Installation:** To use PyXA examples in this skill, see the installation instructions in `automating-mac-apps` skill (PyXA Installation section).

## Core framing
- Pages dictionary is AppleScript-first; discover there.
- JXA provides the logic and data handling.
- **Objects are specifiers**: References to Pages elements that require methods for reads (e.g., `doc.body.text()`) and assignments for writes (e.g., `doc.body.text = 'new text'`).

### Example: Create Document
```javascript
const pages = Application('Pages');
const doc = pages.Document({templateName: 'Blank'});
pages.documents.push(doc);
doc.body.text = "Hello World";
```

## Workflow (default)
1) **Discover**: Open Script Editor > File > Open Dictionary > Pages.
2) **Prototype**: Write minimal AppleScript to verify the command works.
3) **Port to JXA**: Convert AppleScript syntax to JXA objects.
   - Example: `make new document` becomes `pages.documents.push(pages.Document())`.
   - Add error handling (try/catch blocks).
4) **Optimize**: Use batch text operations when possible to avoid performance penalties.
5) **Fallback**: Use AppleScript bridge or UI scripting for dictionary gaps (e.g., specific layout changes).

## Common Pitfalls
- **Dictionary gaps**: Some features (like sophisticated layout adjustments) aren't in the dictionary. Use the AppleScript bridge or UI scripting.
- **Permissions**: Ensure 'Accessibility' settings are enabled for UI scripting.
- **Saving**: Always use `doc.save({in: file_path})` with a valid path object.

## What to load
### Level 1: Basics
- JXA Pages basics: `automating-pages/references/pages-basics.md` (Core objects and document lifecycle)

### Level 2: Recipes & Common Tasks
- Recipes (templates, export, text): `automating-pages/references/pages-recipes.md` (Standard operations)
- Export options matrix: `automating-pages/references/pages-export-matrix.md` (PDF, Word, ePub formats)
- Template strategy: `automating-pages/references/pages-template-strategy.md` (Managing custom templates)

### Level 3: Advanced
- Advanced patterns (tables, images, AppleScript bridge): `automating-pages/references/pages-advanced.md` (Complex integrations)
- UI scripting patterns: `automating-pages/references/pages-ui-scripting.md` (Fallbacks)
- Dictionary translation table: `automating-pages/references/pages-dictionary.md` (AppleScript to JXA mapping)
- PyXA (Python) alternative: `automating-pages/references/pages-pyxa.md`