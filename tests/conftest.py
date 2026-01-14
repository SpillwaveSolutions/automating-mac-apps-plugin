import pathlib
import sys

# Ensure project root is on sys.path for integration tests that import helpers.
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
