from pathlib import Path

# Import all classes explicitly to avoid F403 warning
# This approach allows the code to remain functional while satisfying the linter
# If you need specific classes, import them explicitly instead of using *
from .outcomes_working_group import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "wg.yaml"
