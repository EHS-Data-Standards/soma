"""Data test."""
import os
import glob
import pytest
from pathlib import Path

import soma.datamodel.soma
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = sorted(
    glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))
    + glob.glob(os.path.join(DATA_DIR_INVALID, '*.json'))
)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files.

    All valid data files are loaded against the Container class (tree_root),
    which holds collections of various measurement types.
    """
    # Use Container as the target class since it's the tree_root
    # that holds all measurement collections
    tgt_class = soma.datamodel.soma.Container
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Test that invalid data files fail to load against the Container class."""
    tgt_class = soma.datamodel.soma.Container
    with pytest.raises(Exception):
        yaml_loader.load(filepath, target_class=tgt_class)


def test_in_vivo_subject_cohort_reference():
    """Test that an InVivoSubject can reference its cohort by ID."""
    subject = yaml_loader.loads(
        "id: SUBJECT:lung\nmember_of_cohort: COHORT:study",
        target_class=soma.datamodel.soma.InVivoSubject,
    )
    assert subject.member_of_cohort == "COHORT:study"
