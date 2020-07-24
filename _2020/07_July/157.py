"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form
racecar, which is a palindrome. daily should return false, since there's no
rearrangement that can form a palindrome.
"""


def permutation_palindrome(s: str) -> bool:
    """Return true if any permutation of s is a palindrome"""
    vals = set()
    for c in s:
        if c in vals:
            vals -= {c}
        else:
            vals.add(c)

    return len(vals) < 2


if __name__ == '__main__':
    assert permutation_palindrome("carrace")
    assert not permutation_palindrome("daily")
