"""
Given an array of integers, write a function to determine whether the array
could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can
modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any
one element to get a non-decreasing array.
"""


def non_dec(l: list) -> bool:
    """Return True if we can make the array non-decreasing"""
    l2 = l[:]
    n = len(l) - 1
    count = 0
    for i in range(n):
        if l[i+1] < l[i]:
            count += 1
            l[i] = l[i+1]

    return count < 2


if __name__ == '__main__':
    print(non_dec([10, 5, 7]))
    print(non_dec([10, 5, 1]))
    print(non_dec([1, 2, 3, 4, 10, 5, 6, 7, 8, 9, 10]))
    print(non_dec([1, 2, 3, 4, 10, 5, 6, 10, 8, 9, 10]))