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


def do_better(s: str, k: int) -> bool:
    """Head from the back and the front and see if we can make a palindrome"""
    if k < 0:
        return False
    head_ptr = 0
    tail_ptr = len(s) - 1
    if len(s) <= 1:
        return True
    while s[head_ptr] == s[tail_ptr]:
        if tail_ptr <= head_ptr:
            return True
        head_ptr += 1
        tail_ptr -= 1
    # If they do not match, try again by popping off the front or back char
    if do_better(s[head_ptr:tail_ptr], k-1):
        return True
    elif do_better(s[head_ptr+1:tail_ptr+1], k-1):
        return True


if __name__ == '__main__':
    assert make_pal("waterrfetawx", 2)
    assert not make_pal("waterrfetawx", 1)
    assert make_pal("waterrfetawx", 3)
    assert do_better("waterrfetawx", 2)
    assert not do_better("waterrfetawx", 1)
    assert do_better("waterrfetawx", 3)
