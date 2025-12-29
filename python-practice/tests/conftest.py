"""Shared pytest fixtures and configuration."""

import pytest
from pathlib import Path


@pytest.fixture
def sample_data_dir():
    """Path to sample data directory."""
    return Path(__file__).parent.parent / "src" / "data"


@pytest.fixture
def sample_csv(sample_data_dir):
    """Path to sample CSV file."""
    return sample_data_dir / "sample.csv"


@pytest.fixture
def sample_json(sample_data_dir):
    """Path to sample JSON config file."""
    return sample_data_dir / "config.json"


@pytest.fixture
def sample_emails(sample_data_dir):
    """Path to sample emails text file."""
    return sample_data_dir / "emails.txt"


@pytest.fixture
def sample_numbers():
    """Sample list of numbers for testing."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def sample_strings():
    """Sample list of strings for testing."""
    return ["hello", "world", "python", "testing", "pytest"]

