"""
Implement integer exponentiation. That is, implement the pow(x, y) function,
where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""


def power(x, y):
    """
    x^y == 2*x ^ y/2 - Fewer multiplications is quicker
    """
    if y < 0:
        return power(1 / x, -y)
    elif y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2 == 0:
        return power(x * x, y // 2)
    else:  # y is odd
        return x * power(x * x, y // 2)


if __name__ == '__main__':
    print(power(7, 30))
    assert power(7, 12) == pow(7, 12)
