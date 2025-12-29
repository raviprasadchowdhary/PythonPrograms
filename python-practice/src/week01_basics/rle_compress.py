"""
Problem 2: String Compression (Run-Length)
Compress "aaabbc" → "a3b2c1"
Concepts: loops, string building
"""


def rle_compress(s: str) -> str:
    """
    Compress a string using run-length encoding.

    Args:
        s: Input string

    Returns:
        Compressed string in format "char+count"

    Examples:
        >>> rle_compress("aaabbc")
        'a3b2c1'
        >>> rle_compress("hello")
        'h1e1l2o1'
    """
    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(f"{s[i-1]}{count}")
            count = 1

    # Don't forget the last group
    result.append(f"{s[-1]}{count}")

    return "".join(result)


if __name__ == "__main__":
    print(rle_compress("aaabbc"))      # a3b2c1
    print(rle_compress("hello"))       # h1e1l2o1
    print(rle_compress("aaaa"))        # a4

