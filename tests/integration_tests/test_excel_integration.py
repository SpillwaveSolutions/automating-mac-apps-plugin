import os
import sys
import pathlib
import subprocess
import pytest

HERE = pathlib.Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent.parent  # automating-mac-apps-plugin
SKILLS_ROOT = PROJECT_ROOT / "plugins" / "automating-mac-apps-plugin" / "skills" / "automating-excel" / "scripts"


@pytest.mark.integration
def test_excel_create_and_export(tmp_path):
    if os.getenv("RUN_INTEGRATION") != "1":
        pytest.skip("Set RUN_INTEGRATION=1 to run integration tests; this opens Excel and writes files.")

    # Ensure Excel is available
    check = subprocess.run(["osascript", "-e", 'id of application "Microsoft Excel"'], capture_output=True, text=True)
    if check.returncode != 0:
        pytest.skip("Microsoft Excel not available or Automation denied.")

    create_script = SKILLS_ROOT / "create_excel_spreadsheet.py"
    export_script = SKILLS_ROOT / "export_excel_to_csv.py"

    xlsx_path = tmp_path / "integration-test.xlsx"
    csv_dir = tmp_path / "csv"

    # Create workbook saved to temp path
    subprocess.run(
        [sys.executable, str(create_script), "Integration Test Workbook", "1", str(xlsx_path)],
        check=True,
    )

    # Export to CSV
    subprocess.run(
        [sys.executable, str(export_script), str(xlsx_path), str(csv_dir)],
        check=True,
    )

    assert xlsx_path.exists(), "Excel workbook was not created"
    csv_files = list(csv_dir.glob("*.csv"))
    assert csv_files, "No CSV files were exported"
