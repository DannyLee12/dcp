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


if __name__ == '__main__':
    assert sqrt_(9) == 3
    assert sqrt_(81) == 9
    assert abs(sqrt_(2.25) - 1.5) < 0.0001
    assert abs(sqrt_(0.36) - 0.6) < 0.001
