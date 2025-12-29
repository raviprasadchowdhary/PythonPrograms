"""
Problem 1: Sum & Average of a List
Write a function stats(nums) returning (sum, avg).
Concepts: loops, arithmetic, list
"""

from typing import List, Tuple


def stats(nums: List[float]) -> Tuple[float, float]:
    """
    Calculate sum and average of a list of numbers.

    Args:
        nums: List of numbers

    Returns:
        Tuple of (sum, average)

    Examples:
        >>> stats([1, 2, 3, 4, 5])
        (15, 3.0)
        >>> stats([10, 20, 30])
        (60, 20.0)
    """
    if not nums:
        return (0, 0)

    total = sum(nums)
    avg = total / len(nums)
    return (total, avg)


if __name__ == "__main__":
    # Example usage
    print(stats([1, 2, 3, 4, 5]))  # (15, 3.0)
    print(stats([10, 20, 30]))     # (60, 20.0)
    print(stats([]))                # (0, 0)

