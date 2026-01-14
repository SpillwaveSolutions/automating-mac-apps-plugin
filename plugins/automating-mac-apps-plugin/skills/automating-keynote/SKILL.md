---
name: automating-keynote
description: Automates Apple Keynote using JXA with AppleScript dictionary discovery. Covers document lifecycle, slides, text, shapes, images, tables, charts, transitions, and UI scripting fallback.
---

# Automating Keynote (JXA-first, AppleScript discovery)

## Contents
- [Relationship to the macOS automation skill](#relationship-to-the-macos-automation-skill)
- [Core framing](#core-framing)
- [Workflow (default)](#workflow-default)
- [Quick Examples](#quick-examples)
- [What to load](#what-to-load)

## Relationship to the macOS automation skill
- This skill focuses on Keynote-specific automation (documents, slides, charts).
- Use `automating-mac-apps` for cross-app workflows or general macOS scripting foundations.
- Assumes Apple Events knowledge from the related skill.

## Core Framing
- JXA (JavaScript for Automation) enables macOS app scripting with JavaScript syntax.
- AppleScript dictionaries define Keynote's object model—discover via Script Editor.
- JXA objects are specifiers: read with methods like `.name()`, write with assignments.
- Production scripts use JXA for reliability; AppleScript for prototyping.

## Workflow (default)
1) Discover terms in Script Editor > File > Open Dictionary > Keynote.
2) Prototype minimal AppleScript: `tell application "Keynote" to get name of document 1`.
3) Port to JXA: `Application("Keynote").documents[0].name()` with try-catch blocks.
4) Validate with read-only probes: `Application("Keynote").documents.length > 0`.
5) Use UI scripting only when dictionary lacks features (e.g. `Application("System Events")`).

## Quick Examples

**Prototype (AppleScript):**
```applescript
tell application "Keynote"
    get name of document 1
end tell
```

**Production (JXA):**
```javascript
const keynote = Application("Keynote");
if (keynote.documents.length > 0) {
    console.log(keynote.documents[0].name());
}
```

**Create Slide:**
```javascript
const doc = keynote.documents[0];
const slide = doc.slides.push(keynote.Slide({baseSlide: doc.masterSlides['Title - Center']}));
slide.defaultTitleItem.objectText = "New Slide";
```

## What to load
- Keynote JXA basics + runtime caveats: `automating-keynote/references/keynote-basics.md`
- Keynote recipes (slides, text, images, export): `automating-keynote/references/keynote-recipes.md`
- Deck generator example: `automating-keynote/references/keynote-deck-generator.md`
- Chart-aware deck pattern: `automating-keynote/references/keynote-chart-aware-deck.md`
- Advanced workflows (charts bridge, magic move, UI scripting): `automating-keynote/references/keynote-advanced.md`
- PyXA (Python) practical examples: `automating-keynote/references/keynote-pyxa.md`
- **PyXA API Reference** (complete class/method docs): `automating-keynote/references/keynote-pyxa-api-reference.md`