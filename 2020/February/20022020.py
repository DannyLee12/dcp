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
    for i in l:
        value_0 *= i

    return [value_0/x for x in l]


def prefix_products(l: list) -> list:
    """
    Storing the prefix products up to i and
    the suffix products from i onwards.
    Solves the case where we aren't allowed to use division
    """
    prefixs = []
    suffixes = []
    n = len(l) - 1
    for i, x in enumerate(l):
        if prefixs:
            prefixs.append(prefixs[-1] * x)
        else:
            prefixs.append(x)
        if suffixes:
            suffixes.append(suffixes[-1] * l[n - i])
        else:
            suffixes.append(l[n - i])

    suffixes = suffixes[::-1]

    result = []
    for i in range(n + 1):
        if i == 0:
            result.append(suffixes[1])
        elif i == n:
            result.append(prefixs[i - 1])
        else:
            result.append(prefixs[i - 1] * suffixes[i + 1])

    return result


if __name__ == '__main__':
    assert brute_force([3, 2, 1]) == [2, 3, 6]
    assert brute_force([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert improved([3, 2, 1]) == [2, 3, 6]
    assert improved([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert prefix_products([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert prefix_products([3, 2, 1]) == [2, 3, 6]
