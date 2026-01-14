# macOS Automation Test Suite

Comprehensive test suite for macOS automation scripts using PyXA and PyObjC.

## Overview

This test suite provides both unit tests (with mocking) and integration tests (with real data creation) for the macOS automation skills.

## Test Structure

```
tests/
├── conftest.py                    # Shared fixtures and utilities
├── pytest.ini                    # Pytest configuration
├── requirements-test.txt         # Test dependencies
├── create_integration_test_data.py  # Creates real test data
├── cleanup_integration_test_data.py # Cleans up test data
├── test_automating_notes/       # Notes automation tests
├── test_automating_calendar/    # Calendar automation tests
├── test_automating_mail/        # Mail automation tests
├── test_automating_numbers/     # Numbers automation tests
├── test_automating_reminders/   # Reminders automation tests
├── test_automating_keynote/     # Keynote automation tests
├── test_automating_excel/       # Excel automation tests
└── integration_tests/           # Full integration tests
```

## Installation

### Poetry (recommended; lives outside the plugin payload)
```bash
cd /path/to/automating-mac-apps-plugin
poetry install --with test
```

### Pip (legacy)
```bash
cd /path/to/automating-mac-apps-plugin/tests
pip install -r requirements-test.txt
```

## Running Tests

### Unit Tests (Mocked)
```bash
# Run all unit tests
poetry run pytest

# Run specific test file
poetry run pytest test_automating_notes/test_create_note.py

# Run with coverage
poetry run pytest --cov=../skills --cov-report=html
```

### Integration Tests (Real Data)
```bash
# Create integration test data
python create_integration_test_data.py

# Clean up test data
python cleanup_integration_test_data.py
```

## Test Categories

### Unit Tests
- **Mock PyXA calls** to avoid actual system modifications
- Test error handling and edge cases
- Verify correct API usage
- Fast execution, no system changes

### Integration Tests
- **Create real data** in macOS apps (Notes, Calendar, Mail, etc.)
- Test end-to-end workflows
- Verify data persistence and retrieval
- Require macOS environment with apps installed

## Test Data Created

When running integration tests, the following test data is created:

### Notes
- Folder: `test-YYYY-MM-DD` (where YYYY-MM-DD is today's date)
- Note: "Integration Test Note - Real Data" with sample content

### Calendar
- Event: "Integration Test Meeting - Real Data"
- Time: Tomorrow 2:00 PM - 3:00 PM
- Location: "Virtual Conference Room (Automated Testing)"
- Attendees: rick@spillwave.com, richardhightower@gmail.com

### Mail
- Email from: rick@spillwave.com
- Email to: richardhightower@gmail.com
- Subject: "Integration Test Email - Real Data"
- Body: Sample test content

### Reminders
- Reminder: "Integration Test Reminder - Real Data"
- Due date: Tomorrow
- Notes: Sample reminder content

### Documents
- **Pages**: "Integration Test Pages Document.pages"
- **Word**: "Integration Test Word Document.docx"
- **Keynote**: "Integration Test Keynote.key" (3 slides)
- **PowerPoint**: "Integration Test PowerPoint.pptx" (3 slides)
- **Numbers**: "Integration Test Numbers.numbers" (sample spreadsheet with headers and data)

## Verification

After creating integration test data, the scripts verify creation by:

1. **Searching notes** for test content
2. **Listing calendar events** to confirm creation
3. **Checking reminders** in the Reminders app
4. **Reading document files** from the file system

## Cleanup

The cleanup script removes all test data:

- Deletes test notes and folders
- Removes calendar events
- Deletes reminders
- Removes document files from ~/Documents (including Numbers spreadsheets)
- Provides manual cleanup instructions for emails

## Security Notes

- **Unit tests are safe** - they use mocks and don't modify system state
- **Integration tests create real data** - use cleanup script to remove test data
- **Email addresses** used are placeholders - replace with actual configured accounts
- **Permissions required** - macOS Automation and Accessibility permissions needed for some tests

## Running on CI/CD

For automated testing environments:

```bash
# Install test dependencies
pip install -r requirements-test.txt

# Run only unit tests (safe for CI)
pytest -m "not integration"

# Skip tests requiring GUI/interactive apps
pytest -k "not gui"
```

## Troubleshooting

### Common Issues

1. **PyXA Import Errors**: Expected in test environment - tests mock PyXA
2. **Permission Denied**: Grant Automation permissions in System Settings
3. **App Not Found**: Ensure target macOS apps are installed
4. **Email Not Sent**: Verify Mail app is configured with test accounts

### Debug Mode

```bash
# Run with detailed output
pytest -v -s

# Run single test with debugging
pytest test_automating_notes/test_create_note.py::TestCreateNote::test_create_note_success -s
```

## Contributing

When adding new tests:

1. Follow the existing structure
2. Use descriptive test names
3. Include docstrings
4. Mock external dependencies
5. Test both success and failure scenarios
6. Update this README if needed
