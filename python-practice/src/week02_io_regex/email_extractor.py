"""
Problem 20: Regex Email Extractor
Find all emails in a text using re.
Concepts: regex patterns, groups
"""

import re
from typing import List


def extract_emails(text: str) -> List[str]:
    """
    Extract all email addresses from text.

    Args:
        text: Input text containing emails

    Returns:
        List of email addresses found

    Examples:
        >>> text = "Contact support@example.com or sales@company.org"
        >>> extract_emails(text)
        ['support@example.com', 'sales@company.org']
    """
    # Email pattern - basic version
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)


if __name__ == "__main__":
    # Test with sample data
    from pathlib import Path

    data_dir = Path(__file__).parent.parent / "data"
    email_file = data_dir / "emails.txt"

    if email_file.exists():
        with open(email_file, 'r') as f:
            text = f.read()

        emails = extract_emails(text)
        print("Found emails:")
        for email in emails:
            print(f"  - {email}")
    else:
        # Manual test
        test_text = "Contact support@example.com or sales@company.org"
        print(extract_emails(test_text))

