"""
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
using only mathematical or bit operations. You can assume b can only be 1 or 0.
"""


def bit_return(x: int, y: int, b: int) -> int:
    """Return x if b is 1 and y if b is 0"""
    return x * b + y * (b ^ 1)


if __name__ == '__main__':
    assert bit_return(5, 10, 1) == 5
    assert bit_return(5, 10, 0) == 10
