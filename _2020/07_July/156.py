"""
Given a positive integer n, find the smallest number of squared integers
which sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
"""
from math import sqrt


def get_integers(n: int) -> int:
    """Return the fewest number of squared integers that add up to n"""
    l = [int(sqrt(n))]
    val = l[0] * l[0]
    index = 0
    while val != n:
        val = sum([x*x for x in l])
        if val > n:
            l[index] -= 1
        elif val < n:
            index += 1
            l.append(l[index - 1])

    return len(l)


if __name__ == '__main__':
    assert get_integers(13) == 2
    assert get_integers(27) == 3
    print(get_integers(1423876482376))
