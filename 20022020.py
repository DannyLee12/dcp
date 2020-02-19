"""
HARD
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def brute_force(l: list) -> list:
    """Bad time complexity, O(N^2)"""
    newlist = []
    for i, _ in enumerate(l):
        total = 1
        for j, x in enumerate(l):
            if i == j:
                continue
            total *= x
        newlist.append(total)
    return newlist


def improved(l: list) -> list:
    """Consider keeping the values and calculating each only once"""
    value_0 = 1
    for i, x in enumerate(l):
        if i == 0:
            continue
        value_0 *= x
    value = l[0] * value_0

    return [value/x for x in l]


def more_improved(l: list) -> list:
    """
    Can we do it in one pass through?
    Space complexity might get poor but we can store the value at each position
    while we loop through the list once
    """
    newlist = [1] * len(l)
    for i, x in enumerate(l):
        newlist[i] = x for x in newlist



if __name__ == '__main__':
    assert brute_force([3, 2, 1]) == [2, 3, 6]
    assert brute_force([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert improved([3, 2, 1]) == [2, 3, 6]
    assert improved([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert more_improved([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    print([1,2,3] * 3)