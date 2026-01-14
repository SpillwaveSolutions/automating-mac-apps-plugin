import os
import sys
import pathlib
import pytest

HERE = pathlib.Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent.parent  # automating-mac-apps-plugin
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import create_integration_test_data
import cleanup_integration_test_data


@pytest.mark.integration
def test_create_and_cleanup_real_data():
    if os.getenv("RUN_INTEGRATION") != "1":
        pytest.skip("Set RUN_INTEGRATION=1 to run integration tests; these create real data.")

    create_integration_test_data.create_real_test_data()
    # Best-effort cleanup; some scripts may not exist for deletions, but file cleanup will run.
    cleanup_integration_test_data.cleanup_test_data()
