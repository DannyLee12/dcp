"""
This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element
sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


def in_set(i: int, s: set, total: int = 0) -> int:
    """Recursively add items in the set"""
    if not i in s:
        return 0
    if i in s:
        s -= {i}
        return total + 1 + in_set(i+1, s) + in_set(i-1, s)


if __name__ == '__main__':
    test_set = {1, 3, 4, 5}
    assert in_set(4, test_set) == 3
    assert in_set(1, test_set) == 1
    l = [100, 4, 200, 1, 3, 2]
    s = set(l)
    max_so_far = 0
    for i in l:
        max_so_far = max(max_so_far, in_set(i, s))

    print(max_so_far)

