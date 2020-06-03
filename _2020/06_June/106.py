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


def hoppable_refuel(l: list) -> bool:
    """Assuming a refuel, can we hop to the end of the list"""
    n = len(l)
    hops = 0
    for i, x in enumerate(l):
        if x > 0:
            hops -= 1
        hops += x
        if x == n - 1:
            return True
        if hops == 0:
            return False

    return True


if __name__ == '__main__':
    assert hoppable([2, 0, 1, 0])
    assert hoppable([1, 1, 0, 1]) is False
    assert hoppable_refuel([2, 0, 1, 0])
    assert hoppable_refuel([1, 1, 0, 1]) is False
