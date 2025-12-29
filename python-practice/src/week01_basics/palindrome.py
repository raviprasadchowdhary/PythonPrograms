"""
Problem 3: Palindrome Checker
Ignore spaces/punctuation; "A man, a plan, a canal: Panama" → True
Concepts: normalization, slicing
"""

import re


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome (ignoring spaces, punctuation, and case).

    Args:
        s: Input string

    Returns:
        True if palindrome, False otherwise

    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    # Check if it reads the same forwards and backwards
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("racecar"))                          # True
    print(is_palindrome("hello"))                            # False
    print(is_palindrome("Was it a car or a cat I saw?"))    # True

