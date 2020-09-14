"""
A permutation can be specified by an array P, where P[i] represents the
location of the element at i in the permutation. For example, [2, 1, 0]
represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. For
example, given the array ["a", "b", "c"] and the permutation [2, 1, 0],
return ["c", "b", "a"].
"""


def permute(array, permutation):
    for i in range(len(array)):
        element, p = array[i], permutation[i]

        while p != i:
            array[p], element = element, array[p]
            permutation[p], p = p, permutation[p]

        array[i], permutation[i] = element, p
    return array


if __name__ == '__main__':
    assert permute(["a", "b", "c"], [2, 1, 0])
