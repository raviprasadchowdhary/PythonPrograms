"""Utility functions for file I/O operations."""

from pathlib import Path
from typing import List


def read_lines(filepath: str) -> List[str]:
    """Read all lines from a file."""
    with open(filepath, 'r') as f:
        return f.readlines()


def write_lines(filepath: str, lines: List[str]) -> None:
    """Write lines to a file."""
    with open(filepath, 'w') as f:
        f.writelines(lines)


def count_file_stats(filepath: str) -> dict:
    """Count lines, words, and characters in a file."""
    with open(filepath, 'r') as f:
        content = f.read()
        lines = content.splitlines()
        words = content.split()

        return {
            'lines': len(lines),
            'words': len(words),
            'characters': len(content)
        }

