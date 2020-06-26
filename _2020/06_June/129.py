"""
Given a real number n, find the square root of n. For example,
given n = 9, return 3.
"""


def sqrt_(n: float) -> float:
    """Return the sqrt of a real number"""
    counter = 1
    while 1:
        x = 0
        while x * x <= n:
            if abs((x * x) - n) < 0.00001:
                return x
            x += counter
        counter /= 10


def sqrt_bs(n: float) -> float:
    """Try a binary search approach"""
    if n < 1:
        return sqrt_(n)
    lower, upper = 1, float("inf")
    while lower * lower < n:
        lower *= 2
    lower /= 2
    upper = lower * 2
    while abs(lower - upper) > 0.001:
        midpoint = (upper + lower) / 2
        if midpoint * midpoint > n:
            upper = midpoint
        elif midpoint * midpoint < n:
            lower = midpoint
        else:
            return midpoint
    return midpoint


if __name__ == '__main__':
    assert sqrt_bs(9) == 3
    assert sqrt_bs(81) == 9
    assert abs(sqrt_bs(2.25) - 1.5) < 0.0001
    assert abs(sqrt_bs(0.36) - 0.6) < 0.0001
    print(sqrt_bs(8))
