"""
Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
from math import floor


def brute_force(l: list, v: int) -> bool:
    """Check all possibilities O(N^2)"""
    n = len(l)
    for i, _ in enumerate(l):
        for j in range(i + 1, n):
            if l[i] + l[j] == v:
                return True
    return False


def check_set(l: list, v: int) -> bool:
    """
    Check that the value that would make it true is in the set O(N)
    Note that making a copy of the list and removing an entry will slow
    down the algorithm
    """
    for x in l:
        s = l[:]
        s.remove(x)
        if v - x in s:
            return True
    return False


def sorting(l: list, v: int) -> bool:
    """Try something with sorting. Sorting is O(N log N) worst case"""
    l.sort()

    def bin_search(l: list, v: int) -> int:
        """
        Binary search for the largest value smaller than the target
        """
        n = len(l)
        L = 0
        R = n - 1
        if v > l[-1]:
            return n - 1
        elif v < l[0]:
            return 0
        while L <= R:
            mid = floor((L + R) / 2)
            if l[mid] < v:
                L = mid + 1
            elif l[mid] > v:
                R = mid - 1
            else:
                return mid
        if l[mid] < v:
            return mid
        else:
            return mid - 1

    val_index = bin_search(l, v)

    def bin_find(l: list, v: int, value: int) -> bool:
        """Look for a value that when added to value returns the value v"""
        n = len(l)
        L = 0
        R = n - 1
        while L < R:
            mid = floor((L+R) / 2)
            if l[mid] + value == v:
                return mid
            if l[mid] < v:
                L = mid + 1
            elif l[mid] > v:
                R = mid - 1

    return False


if __name__ == '__main__':
    assert brute_force([10, 15, 3, 7], 17)
    assert not brute_force([10, 15, 3, 7], 6)
    assert check_set([10, 15, 3, 7], 17)
    assert not check_set([10, 15, 3, 7], 6)
    # sorting([10, 15, 3, 7], 17)
    sorting([10, 15, 3, 7], 6)
