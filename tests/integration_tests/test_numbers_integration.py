import os
import sys
import pathlib
import subprocess
import pytest

HERE = pathlib.Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent.parent
SKILLS_ROOT = PROJECT_ROOT / "plugins" / "automating-mac-apps-plugin" / "skills" / "automating-numbers" / "scripts"

@pytest.mark.integration
def test_numbers_create_and_export(tmp_path):
    """Test creating a Numbers spreadsheet and exporting it to CSV"""
    if os.getenv("RUN_INTEGRATION") != "1":
        pytest.skip("Set RUN_INTEGRATION=1 to run integration tests")

    # Check if Numbers is available
    check = subprocess.run(["osascript", "-e", 'id of application "Numbers"'],
                         capture_output=True, text=True)
    if check.returncode != 0:
        pytest.skip("Numbers not available or Automation denied.")

    # Paths to scripts
    create_script = SKILLS_ROOT / "create_numbers_spreadsheet.py"
    export_script = SKILLS_ROOT / "export_numbers_to_csv.py"

    numbers_path = tmp_path / "integration-test.numbers"
    csv_path = tmp_path / "integration-test.csv"

    # Create Numbers spreadsheet
    subprocess.run(
        [sys.executable, str(create_script), "Integration Test Numbers", str(numbers_path)],
        check=True,
    )

    # Export to CSV
    subprocess.run(
        [sys.executable, str(export_script), str(numbers_path), str(csv_path)],
        check=True,
    )

    # Verify files were created
    assert numbers_path.exists(), "Numbers file was not created"
    assert csv_path.exists(), "CSV file was not created"

    # Verify CSV content (basic check)
    with open(csv_path, 'r') as f:
        content = f.read()
        assert "Product" in content, "CSV should contain header"
        assert "Widget A" in content, "CSV should contain sample data"


@pytest.mark.integration
def test_numbers_read_spreadsheet(tmp_path):
    """Test reading data from a Numbers spreadsheet"""
    if os.getenv("RUN_INTEGRATION") != "1":
        pytest.skip("Set RUN_INTEGRATION=1 to run integration tests")

    # Check if Numbers is available
    check = subprocess.run(["osascript", "-e", 'id of application "Numbers"'],
                         capture_output=True, text=True)
    if check.returncode != 0:
        pytest.skip("Numbers not available or Automation denied.")

    # Paths to scripts
    create_script = SKILLS_ROOT / "create_numbers_spreadsheet.py"
    read_script = SKILLS_ROOT / "read_numbers_spreadsheet.py"

    numbers_path = tmp_path / "read-test.numbers"

    # Create Numbers spreadsheet first
    subprocess.run(
        [sys.executable, str(create_script), "Read Test Numbers", str(numbers_path)],
        check=True,
    )

    # Read the spreadsheet
    result = subprocess.run(
        [sys.executable, str(read_script), str(numbers_path)],
        capture_output=True, text=True, check=True,
    )

    # Verify the script ran successfully
    assert result.returncode == 0, f"Read script failed: {result.stderr}"
    assert "Successfully read Numbers spreadsheet data" in result.stdout


@pytest.mark.integration
def test_numbers_create_without_save_path(tmp_path):
    """Test creating a Numbers spreadsheet without specifying save path"""
    if os.getenv("RUN_INTEGRATION") != "1":
        pytest.skip("Set RUN_INTEGRATION=1 to run integration tests")

    # Check if Numbers is available
    check = subprocess.run(["osascript", "-e", 'id of application "Numbers"'],
                         capture_output=True, text=True)
    if check.returncode != 0:
        pytest.skip("Numbers not available or Automation denied.")

    create_script = SKILLS_ROOT / "create_numbers_spreadsheet.py"

    # Create Numbers spreadsheet without save path (should work)
    result = subprocess.run(
        [sys.executable, str(create_script), "Temp Numbers Document"],
        capture_output=True, text=True, check=True,
    )

    # Verify the script ran successfully
    assert result.returncode == 0, f"Create script failed: {result.stderr}"
    assert "Successfully created Numbers spreadsheet" in result.stdout