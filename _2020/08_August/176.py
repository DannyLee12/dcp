"""
Determine whether there exists a one-to-one character mapping from one string
s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b,
b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two
characters.
"""


def map_chars(s1: str, s2: str) -> bool:
    """Return whether we can map chars from s1 to s2"""
    d = {}  # Set of mapped chars
    for x, y in zip(s1, s2):
        if x in d:
            if d[x] != y:
                return False
        else:
            d[x] = y

    return True


if __name__ == '__main__':
    assert map_chars("abc", "bcd")
    assert not map_chars("foo", "bar")
    assert map_chars("abcdefghijklmnopqrstuvwxyzabc",
                     "ghijklmnopqrstuvwxyzabcdef")
    assert not map_chars("abcdefghijjlmnopqrstuvwxyzabc",
                         "ghijklmnopqrstuvwxyzabcdef")
