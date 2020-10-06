"""
Given a string with repeated characters, rearrange the string so that no two
adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return
None.
"""
from collections import defaultdict


def rearrange(s: str) -> str:
    """Rearrange a string so that no adjacent letters are the same"""
    d = defaultdict(int)
    for x in s[1:]:
        d[x] += 1

    s2 = s[0]
    while any(x > 0 for x in d.values()):
        changed = False
        for k in d.keys():
            if k != s2[-1] and d[k] > 0:
                s2 += k
                d[k] -= 1
                changed = True
        if not changed:
            return None

    return s2


if __name__ == '__main__':
    assert rearrange("aaabbc") == "abcaba"
    assert rearrange("aaab") is None
