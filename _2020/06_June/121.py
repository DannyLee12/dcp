"""
Given a string which we can delete at most k, return whether you can make a
palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get
'waterretaw'.
"""


def is_pal(s: str) -> bool:
    """Return True if s is an palindrome"""
    return s == s[::-1]


def make_pal(s: str, k: int) -> bool:
    """Can we make a palindrome by removing a char"""
    if is_pal(s):
        return True
    if k == 0:
        return False
    n = len(s)
    for i in range(n):
        if make_pal(s[:i] + s[i+1:], k-1):
            return True
    return False


if __name__ == '__main__':
    assert make_pal("waterrfetawx", 2)
    assert not make_pal("waterrfetawx", 1)
    assert make_pal("waterrfetawx", 3)
