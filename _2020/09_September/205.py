"""
Given an integer, find the next permutation of it in absolute order. For
example, given 48975, the next permutation would be 49578.
"""

from itertools import permutations
from math import inf


def next_perm(i: int):
    """Return the next perm in absolute order"""
    perms = permutations(str(i))
    current = inf

    for perm in perms:
        val = int("".join(perm))
        if current > val > i:
            current = val

    return current


if __name__ == '__main__':
    assert next_perm(312) == 321
    assert next_perm(123) == 132
    assert next_perm(321) == inf
    assert next_perm(48975) == 49578
