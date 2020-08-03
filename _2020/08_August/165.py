"""
Given an array of integers, return a new array where each element in the new
array is the number of smaller elements to the right of that element in the
original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

    There is 1 smaller element to the right of 3
    There is 1 smaller element to the right of 4
    There are 2 smaller elements to the right of 9
    There is 1 smaller element to the right of 6
    There are no smaller elements to the right of 1

"""


def count_smaller_elements(l: list) -> list:
    """Return a list with the number of elements smaller than the number"""
    nl = []
    n = len(l)
    for i, x in enumerate(l):
        total = 0
        for j in range(i, n):
            if l[j] < x:
                total += 1
        nl.append(total)

    return nl


if __name__ == '__main__':
    assert count_smaller_elements([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
