"""
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""

from math import gcd


def greatest_common_denominator(l: list) -> int:
    """Return the gcd of an entire list"""
    g = l[0]
    n = len(l)
    for i in range(n):
        g = gcd(g, l[i])

    return g


if __name__ == '__main__':
    assert greatest_common_denominator([42, 56, 14]) == 14
    assert greatest_common_denominator([10, 100, 1000]) == 10
    assert greatest_common_denominator([1000, 2000, 5]) == 5
