---
name: doc-to-deck
description: Turn a Pages or Word document into a compelling slide deck
parameters:
  - name: file
    description: Path to the source document (.pages or .docx)
    required: true
  - name: output
    description: Output .key path (optional)
    required: false
  - name: theme
    description: Keynote theme name (optional)
    required: false
  - name: image-mode
    description: Image generation mode: auto|off
    required: false
  - name: slides-per-section
    description: Slides per section (optional)
    required: false
skills:
  - automating-pages
  - automating-word
  - automating-keynote
  - automating-powerpoint
  - automating-mac-apps
---

# Document to Deck

Creates a Keynote deck from a Pages or Word document, with optional image generation if available.

## Usage
```
/doc-to-deck --file /path/to/input.pages
```

## Behavior
1) Extracts structure (headings, sections, key points).
2) Builds a slide outline and key visuals.
3) Generates a Keynote deck with charts and images when appropriate.
