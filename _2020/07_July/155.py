"""
Given a list of elements, find the majority element, which appears more than
half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""
from collections import defaultdict


def mode(l: list) -> int:
    """Return the value that appears more than half the time"""
    d = defaultdict(int)
    for x in l:
        d[x] += 1
        if d[x] >= len(l) // 2:
            return x


if __name__ == '__main__':
    assert(mode([1, 2, 1, 1, 3, 4, 0])) == 1
