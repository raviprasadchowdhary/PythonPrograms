"""Tests for Problem 1: Sum & Average of a List"""

import pytest
from src.week01_basics.stats import stats


class TestStats:
    """Test suite for stats function."""

    @pytest.mark.parametrize("nums,expected_sum,expected_avg", [
        ([1, 2, 3, 4, 5], 15, 3.0),
        ([10, 20, 30], 60, 20.0),
        ([100], 100, 100.0),
        ([0, 0, 0], 0, 0.0),
        ([-1, 1], 0, 0.0),
        ([2.5, 3.5], 6.0, 3.0),
    ])
    def test_stats_valid_input(self, nums, expected_sum, expected_avg):
        """Test stats with valid inputs."""
        result_sum, result_avg = stats(nums)
        assert result_sum == expected_sum
        assert result_avg == expected_avg

    def test_stats_empty_list(self):
        """Test stats with empty list."""
        result_sum, result_avg = stats([])
        assert result_sum == 0
        assert result_avg == 0

    def test_stats_negative_numbers(self):
        """Test stats with negative numbers."""
        result_sum, result_avg = stats([-5, -10, -15])
        assert result_sum == -30
        assert result_avg == -10.0

    def test_stats_large_numbers(self):
        """Test stats with large numbers."""
        nums = [1000000, 2000000, 3000000]
        result_sum, result_avg = stats(nums)
        assert result_sum == 6000000
        assert result_avg == 2000000.0

