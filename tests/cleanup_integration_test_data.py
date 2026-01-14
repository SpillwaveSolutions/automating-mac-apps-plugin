#!/usr/bin/env python3
"""
Clean Up Integration Test Data
Removes all test data created during integration testing
"""

import subprocess
import sys
import os
from datetime import datetime

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

def run_script(skill, script, *args):
    """Run an automation script and return success status"""
    script_path = os.path.join(PROJECT_ROOT, 'plugins', 'automating-mac-apps-plugin', 'skills', skill, 'scripts', script)
    cmd = [sys.executable, script_path] + list(args)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✓ {skill}/{script}: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {skill}/{script} failed: {e.stderr.strip()}")
        return False
    except FileNotFoundError:
        print(f"⚠ {skill}/{script}: Script not found, skipping")
        return False

def cleanup_test_data():
    """Clean up all test data created during integration testing"""
    today = datetime.now()
    test_date = today.strftime('%Y-%m-%d')
    test_folder = f"test-{test_date}"

    print(f"Cleaning up integration test data for {test_date}...")
    print("=" * 60)

    # 1. Clean up Notes
    print("\n📝 CLEANING NOTES")
    print("-" * 25)

    # Delete test note
    success = run_script("automating-notes", "delete_note.py", "Integration Test Note - Real Data")
    if not success:
        print("   Note: delete_note.py script may not exist, manual cleanup required")

    # Delete test folder
    success = run_script("automating-notes", "delete_notes_folder.py", test_folder)
    if not success:
        print("   Note: delete_notes_folder.py script may not exist, manual cleanup required")

    # 2. Clean up Calendar Events
    print("\n📅 CLEANING CALENDAR EVENTS")
    print("-" * 35)
    success = run_script("automating-calendar", "delete_calendar_events.py", "Integration Test Meeting")
    if not success:
        print("   Note: delete_calendar_events.py script exists but failed, or may need manual cleanup")

    # 3. Clean up Reminders
    print("\n⏰ CLEANING REMINDERS")
    print("-" * 25)
    success = run_script("automating-reminders", "delete_reminder.py", "Integration Test Reminder")
    if not success:
        print("   Note: delete_reminder.py script may not exist, manual cleanup required")

    # 4. Clean up Documents (File System)
    print("\n📄 CLEANING DOCUMENT FILES")
    print("-" * 35)

    documents_dir = os.path.expanduser("~/Documents")
    test_files = [
        "Integration Test Pages Document.pages",
        "Integration Test Word Document.docx",
        "Integration Test Keynote.key",
        "Integration Test PowerPoint.pptx",
        "Integration Test Numbers.numbers"
    ]

    files_removed = 0
    for filename in test_files:
        file_path = os.path.join(documents_dir, filename)
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"✓ Removed: {filename}")
                files_removed += 1
            except Exception as e:
                print(f"✗ Failed to remove {filename}: {e}")
        else:
            print(f"⚠ Not found: {filename}")

    # 5. Email Cleanup Note
    print("\n📧 EMAIL CLEANUP")
    print("-" * 20)
    print("   Note: Email cleanup requires manual deletion from Mail app")
    print("   Look for emails with subject: 'Integration Test Email - Real Data'")

    print("\n" + "=" * 60)
    print("✓ CLEANUP COMPLETE!")
    print(f"Date cleaned: {test_date}")
    print(f"Files removed: {files_removed}")
    print("\nManual cleanup may be required for:")
    print("  • Notes: Delete 'Integration Test Note - Real Data' and folder 'test-{test_date}'")
    print("  • Calendar: Delete 'Integration Test Meeting - Real Data' event")
    print("  • Reminders: Delete 'Integration Test Reminder - Real Data'")
    print("  • Mail: Delete test emails manually")

def confirm_cleanup():
    """Get user confirmation before cleanup"""
    print("⚠️  WARNING: This will delete all integration test data!")
    print("This includes:")
    print("  • Test notes and folders")
    print("  • Calendar events")
    print("  • Reminders")
    print("  • Document files")
    print()
    response = input("Are you sure you want to proceed? (yes/no): ").strip().lower()
    return response == 'yes'

if __name__ == "__main__":
    if confirm_cleanup():
        cleanup_test_data()
    else:
        print("Cleanup cancelled.")
