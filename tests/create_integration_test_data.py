#!/usr/bin/env python3
"""
Create Integration Test Data
Creates real test data for calendar, mail, and documents while using mocks for other operations
"""

import subprocess
import sys
import os
from datetime import datetime, timedelta

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

def run_script(skill, script, *args):
    """Run an automation script and return success status and output"""
    script_path = os.path.join(PROJECT_ROOT, 'plugins', 'automating-mac-apps-plugin', 'skills', skill, 'scripts', script)
    cmd = [sys.executable, script_path] + list(args)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✓ {skill}/{script}: {result.stdout.strip()}")
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"✗ {skill}/{script} failed: {e.stderr.strip()}")
        return False, e.stderr.strip()
    except FileNotFoundError:
        print(f"✗ {skill}/{script}: Script not found at {script_path}")
        return False, "Script not found"

def create_real_test_data():
    """Create actual test data for integration testing"""
    today = datetime.now()
    test_date = today.strftime('%Y-%m-%d')
    test_folder = f"test-{test_date}"

    print(f"Creating real integration test data for {test_date}...")
    print("=" * 60)

    # 1. Notes Testing (Real)
    print("\n📝 NOTES TESTING")
    print("-" * 30)
    success, output = run_script("automating-notes", "create_notes_folder.py", test_folder)
    if success:
        success, output = run_script("automating-notes", "create_note.py",
                                   "Integration Test Note - Real Data",
                                   "This note was created during real integration testing on " + test_date + ". It contains sample content to verify that the PyXA Notes automation is working correctly.",
                                   test_folder)

        # Verify creation by searching
        if success:
            success, output = run_script("automating-notes", "search_notes.py", "Integration Test Note")
            print(f"   Verification: Found {len(output.split('Integration Test Note')) - 1} matching notes")

    # 2. Calendar Testing (Real)
    print("\n📅 CALENDAR TESTING")
    print("-" * 30)
    tomorrow = today + timedelta(days=1)
    start_time = tomorrow.replace(hour=14, minute=0).isoformat()
    end_time = tomorrow.replace(hour=15, minute=0).isoformat()

    success, output = run_script("automating-calendar", "create_calendar_event.py",
                               "Integration Test Meeting - Real Data",
                               start_time, end_time,
                               "Virtual Conference Room (Automated Testing)",
                               "rick@spillwave.com", "richardhightower@gmail.com")

    if success:
        # Verify by listing upcoming events
        success, output = run_script("automating-calendar", "list_upcoming_events.py")
        if "Integration Test Meeting" in output:
            print("   ✓ Event verified in calendar")
        else:
            print("   ⚠ Event creation succeeded but verification failed")

    # 3. Mail Testing (Real)
    print("\n📧 MAIL TESTING")
    print("-" * 30)
    success, output = run_script("automating-mail", "create_email.py",
                               "rick@spillwave.com",
                               "richardhightower@gmail.com",
                               "Integration Test Email - Real Data",
                               "This is a real test email sent during integration testing on " + test_date + ". It verifies that the PyXA Mail automation can successfully send emails between configured accounts.")

    if success:
        print("   ✓ Email sent successfully (check your Mail app for confirmation)")

    # 4. Reminders Testing (Real)
    print("\n⏰ REMINDERS TESTING")
    print("-" * 30)
    due_date = tomorrow.strftime('%Y-%m-%d')

    success, output = run_script("automating-reminders", "create_reminder.py",
                               "Integration Test Reminder - Real Data",
                               "This reminder was created during automated testing on " + test_date + ". It tests the PyXA Reminders integration.",
                               due_date)

    if success:
        # Verify by listing reminders
        success, output = run_script("automating-reminders", "list_reminders.py")
        if "Integration Test Reminder" in output:
            print("   ✓ Reminder verified in Reminders app")
        else:
            print("   ⚠ Reminder creation succeeded but verification failed")

    # 5. Document Creation Testing (Real)
    print("\n📄 DOCUMENT CREATION TESTING")
    print("-" * 30)

    # Pages document
    success, output = run_script("automating-pages", "create_document.py",
                               "Integration Test Pages Document - Real Data",
                               "This is a Pages document created during automated testing on " + test_date + ".\n\nIt includes multiple paragraphs to test document creation and formatting.\n\nThis verifies that the PyXA Pages integration works correctly.")

    # Word document
    success, output = run_script("automating-word", "create_document.py",
                               "Integration Test Word Document - Real Data",
                               "This is a Word document created during automated testing on " + test_date + ".\n\nIt includes multiple paragraphs to test document creation and formatting.\n\nThis verifies that the PyXA Word integration works correctly.")

    # Keynote presentation
    keynote_content = """# Slide 1
# Integration Test Keynote Presentation

Welcome to our automated testing presentation!
Created on: """ + test_date + """

This presentation was generated automatically to test Keynote integration.

# Slide 2
# Testing Features

- Automatic slide creation
- Multi-line content support
- Formatting verification
- PyXA Keynote integration

# Slide 3
# Test Results

✓ Slide creation successful
✓ Content insertion working
✓ Keynote automation verified

Thank you for testing!
"""

    success, output = run_script("automating-keynote", "create_keynote_presentation.py",
                               "Integration Test Keynote - Real Data",
                               keynote_content)

    # PowerPoint presentation
    powerpoint_content = """# Slide 1
# Integration Test PowerPoint Presentation

Welcome to PowerPoint automated testing!
Created on: """ + test_date + """

This presentation tests PowerPoint integration with PyXA.

# Slide 2
# Automation Features

- Programmatic slide generation
- Content insertion
- Cross-platform compatibility
- Microsoft Office integration

# Slide 3
# Verification Complete

✓ PowerPoint automation working
✓ Slide creation successful
✓ Content properly formatted

Test completed successfully!
"""

    success, output = run_script("automating-powerpoint", "create_presentation.py",
                               "Integration Test PowerPoint - Real Data",
                               powerpoint_content)

    print("\n" + "=" * 60)
    print("✓ INTEGRATION TEST DATA CREATION COMPLETE!")
    print(f"Test folder created: {test_folder}")
    print("\nCreated test data includes:")
    print("  • Notes in folder: test-{test_date}")
    print("  • Calendar event: Integration Test Meeting")
    print("  • Email: Integration Test Email")
    print("  • Reminder: Integration Test Reminder")
    print("  • Documents: Pages, Word, Keynote, and PowerPoint files")
    print("\nTo clean up all test data: run 'python cleanup_integration_test_data.py'")

def read_back_created_content():
    """Read back and verify created content"""
    print("\n🔍 VERIFYING CREATED CONTENT")
    print("-" * 40)

    # Read notes
    print("\n📝 Checking Notes...")
    success, output = run_script("automating-notes", "search_notes.py", "Integration Test")
    if success and output.strip():
        note_count = len([line for line in output.split('\n') if 'Integration Test' in line])
        print(f"   Found {note_count} test notes")
        print(f"   Sample: {output[:100]}...")
    else:
        print("   No test notes found or search failed")

    # Read calendar events
    print("\n📅 Checking Calendar Events...")
    success, output = run_script("automating-calendar", "list_upcoming_events.py")
    if success and "Integration Test Meeting" in output:
        print("   ✓ Test calendar event found")
        # Extract event details
        lines = output.split('\n')
        for line in lines:
            if "Integration Test Meeting" in line:
                print(f"   Event: {line.strip()}")
                break
    else:
        print("   ✗ Test calendar event not found")

    # Read reminders
    print("\n⏰ Checking Reminders...")
    success, output = run_script("automating-reminders", "list_reminders.py")
    if success and "Integration Test Reminder" in output:
        print("   ✓ Test reminder found")
    else:
        print("   ✗ Test reminder not found")

    print("\n📄 Document files should be created in your Documents folder")
    print("   Check for: Integration Test Pages Document.pages")
    print("   Check for: Integration Test Word Document.docx")
    print("   Check for: Integration Test Keynote.key")
    print("   Check for: Integration Test PowerPoint.pptx")

if __name__ == "__main__":
    create_real_test_data()
    read_back_created_content()