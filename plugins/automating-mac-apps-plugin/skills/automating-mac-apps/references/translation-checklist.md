# AppleScript -> JXA Translation Checklist

Use this after prototyping in AppleScript.

## Core mapping
- `tell application "App"` -> `const app = Application("App");`
- Property reads: `name of doc` -> `doc.name()`
- Property writes: `set name of doc to "X"` -> `doc.name = "X"`
- Collections: `every document` -> `app.documents()`
- Indexing: `document 1` -> `app.documents[0]`
- Current/front: `front window` -> `app.windows[0]`

## Verification steps
- Confirm dictionary terms in Script Editor.
- Replace AppleScript `whose` with JS `filter` or `whose` calls.
- Ensure final output is `JSON.stringify(...)`.
- Ensure `console.log` is only for debug (stderr).

## Common pitfalls
- JXA collections are often functions, not properties.
- JXA property reads are methods; writes are assignments.
- UI scripting requires `System Events` + accessibility permissions.
- `delay()` is seconds, not milliseconds.

## Common pitfalls (expanded)
- `console.log` writes to stderr; stdout should be JSON.
- Use `Path(...)` for file references when required by app dictionaries.
- `app.windows[0]` fails if no windows; check length first.
- `whose` filters can be slower than JS `filter` on large collections.
