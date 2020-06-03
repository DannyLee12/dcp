"""
Given an integer list where each number represents the number of hops you can
make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""


def hoppable(l: list) -> bool:
    """Return whether we can hop to the end of the list"""
    n = len(l)
    pos = 0
    hops = l[pos]
    while hops:
        pos = pos + hops
        if pos >= n-1:
            return True
        hops = l[pos]

    return False


if __name__ == '__main__':
    assert hoppable([2, 0, 1, 0])
    assert hoppable([1, 1, 0, 1]) is False
