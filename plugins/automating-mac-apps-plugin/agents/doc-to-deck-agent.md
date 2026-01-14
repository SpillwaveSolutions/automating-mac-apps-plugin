---
name: doc-to-deck-agent
description: Converts a Pages or Word document into a Keynote slide deck
triggers:
  - pattern: "doc to deck"
    type: keyword
  - pattern: "pages to keynote"
    type: keyword
  - pattern: ".docx"
    type: file_mention
  - pattern: ".pages"
    type: file_mention
  - pattern: "slide deck"
    type: keyword
skills:
  - automating-pages
  - automating-word
  - automating-keynote
  - automating-powerpoint
  - automating-mac-apps
---

# Doc to Deck Agent

Builds a slide deck from a document and adds visuals when possible.
