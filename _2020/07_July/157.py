"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form
racecar, which is a palindrome. daily should return false, since there's no
rearrangement that can form a palindrome.
"""
from collections import defaultdict


def permutation_palindrome(s: str) -> bool:
    """Return true if any permutation of s is a palindrome"""
    d = defaultdict(int)
    for c in s:
        d[c] += 1

    odds = 0
    for v in d.values():
        if v % 2 == 1:  # Odd number
            odds += 1
            if odds > 1:
                return False
    return True


if __name__ == '__main__':
    assert permutation_palindrome("carrace")
    assert not permutation_palindrome("daily")
