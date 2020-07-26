"""


This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is
no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef",
return null.
"""


def first_recurring(s: str) -> str:
    """Return the first reccurring character in a string"""
    chars = set()
    for c in s:
        if c in chars:
            return c
        chars.add(c)

    return None


if __name__ == '__main__':
    assert first_recurring("acbbac") == "b"
    assert first_recurring("qwerty") is None
