---
name: contact-upsert
description: Create or update a contact, optionally assign to groups
parameters:
  - name: name
    description: Full name of the contact
    required: true
  - name: email
    description: Primary email
    required: true
  - name: phone
    description: Phone number (optional)
    required: false
  - name: organization
    description: Company/organization (optional)
    required: false
  - name: title
    description: Job title (optional)
    required: false
  - name: groups
    description: Comma-separated groups to ensure membership (optional)
    required: false
skills:
  - automating-contacts
  - automating-mac-apps
---

# Contact Upsert

Creates or updates a contact by email, sets core fields, and ensures group membership.

## Usage
```
/contact-upsert --name "Ada Lovelace" --email ada@example.com \
  --phone "+1-555-123-4567" --organization "Analytical Engine" \
  --title "Engineer" --groups "VIP,Engineering"
```

## Behavior
1) Finds an existing contact by email (server-side filter).  
2) If found, updates name/org/title/phone; if not, creates a new contact.  
3) Adds email/phone as multi-value elements (no overwrite of other values).  
4) Ensures membership in the provided groups (creates groups if missing).  
5) Saves changes via Contacts.
