"""
Given an array of integers out of order, determine the bounds of the smallest
window that must be sorted in order for the entire array to be sorted.
For example, given [3, 7, 5, 6, 9], you should return (1, 3).
"""


def get_bounds(l: list) -> (int, int):
    """
    Return the bounds of the smallest window that must be sorted for
    the entire array to be sorted
    """
    def is_sorted(l1):
        """Is l1 sorted?"""
        return sorted(l1) == l1

    n = len(l)
    s = 0
    e = n
    start = True
    while s < e:
        if start and is_sorted(l[:s] + sorted(l[s:e]) + l[e:]):
            s += 1
        elif start:
            start = False
            s -= 1
            e -= 1
        else:
            if is_sorted(l[:s] + sorted(l[s:e]) + l[e:]):
                e -= 1
            else:
                return s, e


if __name__ == '__main__':
    assert get_bounds([3, 7, 5, 6, 9]) == (1, 3)
