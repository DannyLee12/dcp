"""
Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
return 0000 1111 0000 1111 0000 1111 0000 1111.
"""


def reverse_bits(i: int) -> int:
    """Return a number with the bits reversed"""
    return i ^ 2 ** 32 - 1


if __name__ == '__main__':
    assert reverse_bits(1) == 2 ** 32 - 1 - 1
    assert reverse_bits(2 ** 32  - 1) == 0
    assert reverse_bits(reverse_bits(10)) == 10

    i1 = int("11110000111100001111000011110000", 2)
    i2 = int("00001111000011110000111100001111", 2)
    assert reverse_bits(i1) == i2
    assert reverse_bits(i2) == i1
