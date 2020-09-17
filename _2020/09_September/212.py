"""
Spreadsheets often use this alphabetical encoding for its columns: "A", "B",
"C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example, given 1,
return "A". Given 27, return "AA".
"""


def get_id(s: str) -> int:
    """Return the numerical value of a column"""
    x = 1
    for c in s:
        x += ord(c) - ord("A")
        x += 26

    return x - 26


if __name__ == '__main__':
    assert get_id("A") == 1
    assert get_id("AA") == 27
    assert get_id("AAA") == 26 + 26 + 1
