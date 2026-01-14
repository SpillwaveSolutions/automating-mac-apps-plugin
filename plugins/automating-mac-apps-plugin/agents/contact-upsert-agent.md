---
name: contact-upsert-agent
description: Creates or updates a contact and assigns groups
triggers:
  - pattern: "add contact"
    type: keyword
  - pattern: "new contact"
    type: keyword
  - pattern: ".vcf"
    type: file_mention
  - pattern: "save to contacts"
    type: keyword
skills:
  - automating-contacts
  - automating-mac-apps
---

# Contact Upsert Agent

Given contact details (name/email required, optional phone/org/title/groups), the agent:
1) Finds or creates the contact by email.  
2) Updates core fields and adds email/phone as multi-values.  
3) Ensures group membership (creates groups if missing).  
4) Saves in Contacts.  

Use with the `contact-upsert` command or when a .vcf or "add contact" request appears.
