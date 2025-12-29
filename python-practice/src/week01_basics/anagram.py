"""
Problem 4: Anagram Checker
"listen" vs "silent" → True (ignore case & spaces)
Concepts: sorting/counters
"""


def is_anagram(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if anagrams, False otherwise

    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("hello", "world")
        False
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))    # False

