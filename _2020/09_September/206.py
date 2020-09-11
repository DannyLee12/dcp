"""
A permutation can be specified by an array P, where P[i] represents the
location of the element at i in the permutation. For example, [2, 1, 0]
represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. For
example, given the array ["a", "b", "c"] and the permutation [2, 1, 0],
return ["c", "b", "a"].
"""


def permute_array(l: list, p: list) -> list:
    """Permute a list based on a permutation list"""
    l2 = ['' for x in range(len(l))]
    for i, x in enumerate(p):
        l2[i] = l[x]

    return l2


if __name__ == '__main__':
    print(permute_array(["a", "b", "c"], [2, 1, 0]))
