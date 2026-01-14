import os
import sys
import pathlib
import subprocess
import pytest

HERE = pathlib.Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent.parent  # automating-mac-apps-plugin
SKILLS_ROOT = PROJECT_ROOT / "plugins" / "automating-mac-apps-plugin" / "skills" / "automating-keynote" / "scripts"

@pytest.mark.integration
def test_keynote_create_and_export(tmp_path):
    if os.getenv("RUN_INTEGRATION") != "1":
        pytest.skip("Set RUN_INTEGRATION=1 to run integration tests; this opens Keynote and writes files.")

    # Ensure Keynote is available
    check = subprocess.run(["osascript", "-e", 'id of application "Keynote"'], capture_output=True, text=True)
    if check.returncode != 0:
        pytest.skip("Keynote not available or Automation denied.")

    # Paths to scripts
    create_script = SKILLS_ROOT / "create_keynote_presentation.py"
    export_script = SKILLS_ROOT / "export_keynote_presentation.py"

    key_path = tmp_path / "integration-test.key"
    pdf_path = tmp_path / "integration-test.pdf"

    # Create presentation saved to temp path
    subprocess.run(
        [sys.executable, str(create_script), "Integration Test Keynote", "", str(key_path)],
        check=True,
    )

    # Export to PDF
    subprocess.run(
        [sys.executable, str(export_script), str(key_path), str(pdf_path), "PDF"],
        check=True,
    )

    assert key_path.exists(), "Keynote file was not created"
    assert pdf_path.exists(), "Exported PDF was not created"
