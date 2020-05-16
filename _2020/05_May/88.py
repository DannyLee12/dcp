"""
Implement division of two positive integers without using the division,
multiplication, or modulus operators. Return the quotient as an integer,
ignoring the remainder.
"""
from random import randint


def division(a: int, b: int) -> int:
    """Return a // b"""
    value = b
    total = 0
    while a >= value:
        if a == value:
            return total + 1
        value += b
        total += 1

    return total


if __name__ == '__main__':
    assert 5 // 4 == division(5, 4)
    assert 3 // 5 == division(3, 5)
    assert division(4, 4) == 1
    assert division(8, 4) == 2
    for _ in range(100):
        a, b = randint(0, 100), randint(0, 100)
        assert a // b == division(a, b)
