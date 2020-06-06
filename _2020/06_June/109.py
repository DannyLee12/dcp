"""
Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd
bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""


def swap_bits(i: int) -> int:
    """Swap Even and Odd bits"""
    l = [x for i, x in enumerate(bin(i)) if i > 1]
    for x in range(0, len(l), 2):
        l[x], l[x+1] = l[x+1], l[x]

    return int("".join(l), 2)


if __name__ == '__main__':
    assert swap_bits(170) == 85
    assert swap_bits(226) == 209
    assert swap_bits(2) == 1
    assert swap_bits(12) == 12
