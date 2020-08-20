"""
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""


def gcd(a, b, ap=None, bp=None):
    """Return the gcd of a and b"""
    if a == b:
        return a
    elif a < b:  # If a < b, switch a and b
        a, b = b, a

    if a % b == 0:
        return b
    if not ap and not bp:
        ap, bp = a, b
    if b + bp <= a:
        return gcd(a, b + bp, ap, bp)
    else:
        return gcd(a + ap, b + bp, ap, bp)


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
