"""
Given an integer n, return the length of the longest consecutive run of 1s in
its binary representation.

For example, given 156, you should return 3.
"""


def consecutive_ones(n: int) -> int:
    """Return the longest consecutive 1s in a binary representation"""
    max_length, length = 0, 0
    for x in bin(n)[2:]:
        if x == '1':
            length += 1
        else:
            max_length = max(max_length, length)
            length = 0

    return max_length


if __name__ == '__main__':
    assert consecutive_ones(156) == 3
