"""
Given two strings A and B, return whether or not A can be shifted some number
of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is
acb, return false.
"""


def can_shift(A: str, B: str) -> bool:
    """Can A be shifted to become B"""
    n = len(A)
    if n != len(B):
        return False
    for i in range(n):
        inx = B.find(A[:n - i - 1])
        if inx != -1:
            if A[i:] == B[:i+1]:
                return True
    return False


if __name__ == '__main__':
    assert can_shift("abcde", "cdeab")
    assert can_shift("abc", "acb") is False
