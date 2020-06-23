"""
This problem was asked by Facebook.

Write a function that rotates a list by k elements. For example,
[1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
Try solving this without creating a copy of the list.
How many swap or move operations do you need?
"""


def rotate(l: list, k: int) -> list:
    """Rotate l by k elements"""
    return l[k:] + l[:k]


def swaps(l:list, k: int) -> list:
    """Rotate using swaps"""
    n = len(l)
    i = 0
    while i < k:
        for x in range(n - 1):
            l[x], l[x+1] = l[x+1], l[x]
        i += 1

    return l


if __name__ == '__main__':
    print(rotate([1, 2, 3, 4, 5, 6], 2))
    print(swaps([1, 2, 3, 4, 5, 6], 2))
