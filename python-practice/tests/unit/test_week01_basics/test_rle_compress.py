"""Tests for Problem 2: String Compression (Run-Length)"""

import pytest
from src.week01_basics.rle_compress import rle_compress


class TestRLECompress:
    """Test suite for rle_compress function."""

    @pytest.mark.parametrize("input_str,expected", [
        ("aaabbc", "a3b2c1"),
        ("hello", "h1e1l2o1"),
        ("aaaa", "a4"),
        ("abc", "a1b1c1"),
        ("aabbcc", "a2b2c2"),
        ("a", "a1"),
    ])
    def test_compress_valid_input(self, input_str, expected):
        """Test compression with valid inputs."""
        assert rle_compress(input_str) == expected

    def test_compress_empty_string(self):
        """Test compression with empty string."""
        assert rle_compress("") == ""

    def test_compress_repeated_pattern(self):
        """Test compression with repeated patterns."""
        assert rle_compress("aaabbbaaabbb") == "a3b3a3b3"

    def test_compress_single_char_repeated(self):
        """Test compression with single character repeated."""
        assert rle_compress("zzzzz") == "z5"

