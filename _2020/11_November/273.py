"""
A fixed point in an array is an element whose value is equal to its index.
Given a sorted array of distinct elements, return a fixed point, if one exists.
Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8],
you should return False.
"""


def value_index(l: list) -> bool:
    """return index = value"""
    for i, x in enumerate(l):
        if i == x:
            return i
    return False


if __name__ == '__main__':
    assert value_index([-6, 0, 2, 40]) == 2
    assert not value_index([1, 5, 7, 8])
