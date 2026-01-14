---
name: automating-contacts
description: Automates macOS Contacts via JXA with AppleScript dictionary discovery. Covers querying, CRUD, multi-value fields, groups, images, and ObjC bridge fallbacks. Use for "JXA contacts automation", "macOS address book scripting", "AppleScript contacts", "Contacts app automation".
---

# Automating Contacts (JXA-first, AppleScript discovery)

## Relationship to Other Skills
- **Standalone for Contacts:** Use this skill for Contacts-specific operations (querying, CRUD, groups).
- **Reuse `automating-mac-apps` for:** TCC permissions setup, shell command helpers, UI scripting fallbacks, and ObjC bridge patterns.
- **Integration:** Load both skills when combining Contacts automation with broader macOS scripting.
- **PyXA Installation:** To use PyXA examples in this skill, see the installation instructions in `automating-mac-apps` skill (PyXA Installation section).

## Core framing
- Contacts dictionary is AppleScript-first; discover terms there, implement in JXA.
- Everything is an object specifier; read with methods (name(), emails()), write with assignments, and push child objects to collections.
- Multi-value fields (emails, phones, addresses, dates) are elements, not scalars; use constructor + `.push()`.
- Group membership uses the `add ... to` command (or `.people.push`), handle duplicates defensively.
- TCC applies: running host (Terminal/Script Editor/app) must have Contacts permission.

## Workflow (default)
1) Inspect the Contacts dictionary in Script Editor (JavaScript view).
2) Prototype minimal AppleScript to validate verbs; port to JXA with specifier reads/writes.
3) Use `.whose` for coarse filtering; fall back to hybrid (coarse filter + JS refine) when needed.
4) Create records with proxy + `make`, then assign primitives and push multi-values; `Contacts.save()` to persist.
5) Verify persistence: check `person.id()` exists after save; handle TCC permission errors.
6) Manage groups after person creation; guard against duplicate membership with existence checks.
7) For photos or broken bridges, use ObjC/clipboard fallback; for heavy queries, batch read or pre-filter.
8) Test operations: run→check results→fix errors in iterative loop.

### Complex Operation Checklist
- [ ] TCC permissions granted for Contacts access
- [ ] Dictionary inspected and verbs validated
- [ ] Test AppleScript prototype runs without errors
- [ ] JXA port handles specifiers correctly
- [ ] Multi-value fields pushed to arrays properly
- [ ] Groups checked for existence before creation
- [ ] Operations saved and verified with `.id()` checks
- [ ] Error handling wrapped in try/catch blocks

## Quickstart (upsert + group)
```javascript
const Contacts = Application("Contacts");
const email = "ada@example.com";
try {
  const existing = Contacts.people.whose({ emails: { value: { _equals: email } } })();
  const person = existing.length ? existing[0] : Contacts.Person().make();
  person.firstName = "Ada";
  person.lastName = "Lovelace";
  
  // Handle multi-value email
  const work = Contacts.Email({ label: "Work", value: email });
  person.emails.push(work);
  Contacts.save();
  
  // Handle groups with error checking
  let grp;
  try { 
    grp = Contacts.groups.byName("VIP"); 
    grp.name(); // Verify exists
  } catch (e) {
    grp = Contacts.Group().make(); 
    grp.name = "VIP";
  }
  Contacts.add(person, { to: grp });
  Contacts.save();
  console.log("Contact upserted successfully");
} catch (error) {
  console.error("Contacts operation failed:", error);
}
```

## Pitfalls (read first)
### TCC Permissions
- Photos/attachments require TCC + Accessibility permissions; use clipboard UI fallback if blocked.

### Data Limitations  
- Yearless birthdays: not cleanly scriptable; expect full dates for reliable operations.
- Geofence or advanced triggers: delegate to Shortcuts app.

### Performance
- Heavy queries: batch read or pre-filter to avoid timeouts.

## When Not to Use
- For non-macOS platforms (use platform-specific APIs)
- When AppleScript-only solutions suffice (skip JXA complexity)
- For Contacts data that requires iCloud sync operations
- When building user-facing apps (use native Contacts framework instead)

## What to load
- JXA basics & specifiers: `automating-contacts/references/contacts-basics.md`
- Recipes (query, create, multi-values, groups): `automating-contacts/references/contacts-recipes.md`
- Advanced (hybrid filters, clipboard image, TCC, date pitfalls): `automating-contacts/references/contacts-advanced.md`
- Dictionary & type map: `automating-contacts/references/contacts-dictionary.md`
- **PyXA API Reference** (complete class/method docs): `automating-contacts/references/contacts-pyxa-api-reference.md`