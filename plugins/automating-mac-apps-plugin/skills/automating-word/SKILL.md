---
name: automating-word
description: Automates Microsoft Word via JXA with AppleScript dictionary discovery. Covers documents, ranges, find/replace, tables, export, and ObjC bridge patterns.
---

# Automating Word (JXA-first, AppleScript discovery)

## Relationship to the macOS automation skill
- Standalone for Word, aligned with `automating-mac-apps` patterns.
- Use `automating-mac-apps` skill for permissions, shell execution, and UI scripting guidance.

## Core framing
- Word dictionary is AppleScript-first; discover there.
- JXA provides logic, data handling, and ObjC bridge access.
- Objects are specifiers; read via methods, write via assignments.
- Handle errors from Word operations using try/catch blocks and Application error checking.

## Implementation Workflow
1. **Discover AppleScript Dictionary:** Open Script Editor, browse Word's AppleScript dictionary to understand available objects and methods.
2. **Translate to JXA:** Use discovered AppleScript syntax as reference for JXA equivalents, consulting the dictionary translation table.
3. **Set Up JXA Script:** Initialize Word application object and document references.
4. **Implement Operations:** Apply find/replace, table manipulation, or export using JXA methods.
5. **Test and Validate:** Run script and verify document changes match expectations.

## Quick Examples

**Basic document opening (JXA - Legacy):**
```javascript
const word = Application('Microsoft Word');
word.documents.open('/path/to/document.docx');
```

**Basic document opening (PyXA - Recommended):**
```python
import PyXA

word = PyXA.Word()
word.documents().open("/path/to/document.docx")
```

**PyObjC with Scripting Bridge:**
```python
from ScriptingBridge import SBApplication

word = SBApplication.applicationWithBundleIdentifier_("com.microsoft.Word")

# Open document
document = word.documents().open_("/path/to/document.docx")
```

**Find and replace (JXA - Legacy):**
```javascript
const range = word.activeDocument.content;
range.find.text = 'old text';
range.find.replacement.text = 'new text';
range.find.execute({replace: 'all'});
```

**Find and replace (PyXA - Recommended):**
```python
import PyXA

word = PyXA.Word()
doc = word.active_document()

# Get document content range
content_range = doc.content()

# Set up find and replace
find_obj = content_range.find()
find_obj.text = 'old text'
find_obj.replacement.text = 'new text'

# Execute replacement
find_obj.execute(replace='all')
```

**PyObjC Find and Replace:**
```python
from ScriptingBridge import SBApplication

word = SBApplication.applicationWithBundleIdentifier_("com.microsoft.Word")

# Get active document
doc = word.activeDocument()

# Get content range
content_range = doc.content()

# Set up find
find_obj = content_range.find()
find_obj.setText_('old text')
find_obj.replacement().setText_('new text')

# Execute replacement
find_obj.executeWithFindText_replacement_replace_(None, None, 'all')
```

**Table creation (JXA - Legacy):**
```javascript
const table = word.activeDocument.tables.add(word.activeDocument.content, 3, 4);
table.cell(1, 1).range.text = 'Header';
```

**Table creation (PyXA - Recommended):**
```python
import PyXA

word = PyXA.Word()
doc = word.active_document()

# Add table with 3 rows, 4 columns
table = doc.tables().add(doc.content(), 3, 4)

# Set header in first cell
cell = table.cell(1, 1)
cell.range().text = 'Header'
```

**PyObjC Table Creation:**
```python
from ScriptingBridge import SBApplication

word = SBApplication.applicationWithBundleIdentifier_("com.microsoft.Word")

# Get active document
doc = word.activeDocument()

# Add table
content = doc.content()
table = doc.tables().add_range_numRows_numColumns_(content, 3, 4)

# Set header text
cell = table.cell_row_column_(1, 1)
cell.range().setText_('Header')
```

## Validation Checklist
After implementing Word automation:
- [ ] Test script execution without errors
- [ ] Verify document changes applied correctly
- [ ] Check ObjC bridge objects return expected values
- [ ] Run find/replace operations and confirm replacements
- [ ] Export documents and validate output formats

## When Not to Use
Avoid this skill for:
- General macOS automation (use `automating-mac-apps`)
- Excel automation (use `automating-excel`)
- Non-Microsoft Office applications
- Web-based document processing

## What to load
- Word JXA basics: `automating-word/references/word-basics.md` (core concepts only; see references for advanced usage)
- Recipes (ranges, find/replace, tables): `automating-word/references/word-recipes.md`
- Advanced patterns (export enums, ObjC bridge): `automating-word/references/word-advanced.md`
- Dictionary translation table: `automating-word/references/word-dictionary.md`
- PyXA (Python) alternative: `automating-word/references/word-pyxa.md`