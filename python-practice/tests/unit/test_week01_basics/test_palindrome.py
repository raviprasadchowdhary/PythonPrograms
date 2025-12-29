"""Tests for Problem 3: Palindrome Checker"""

import pytest
from src.week01_basics.palindrome import is_palindrome


class TestPalindrome:
    """Test suite for is_palindrome function."""

    @pytest.mark.parametrize("input_str,expected", [
        ("A man, a plan, a canal: Panama", True),
        ("racecar", True),
        ("hello", False),
        ("Was it a car or a cat I saw?", True),
        ("Madam", True),
        ("python", False),
        ("", True),  # Empty string is palindrome
        ("a", True),
        ("ab", False),
        ("aba", True),
    ])
    def test_palindrome(self, input_str, expected):
        """Test palindrome checker with various inputs."""
        assert is_palindrome(input_str) == expected

    def test_palindrome_with_numbers(self):
        """Test palindrome with numbers."""
        assert is_palindrome("12321") == True
        assert is_palindrome("12345") == False

    def test_palindrome_mixed_alphanumeric(self):
        """Test palindrome with mixed alphanumeric."""
        assert is_palindrome("A1B2C2B1A") == True

