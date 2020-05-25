"""
Given a number represented by a list of digits, find the next greater
permutation of a number, in terms of lexicographic ordering. If there is not
greater permutation possible, return the permutation with the lowest
value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should
return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the
input memory)?
"""

import itertools


def greater_perm(l: list) -> list:
    """Return the nex greater perm"""
    perms = itertools.permutations(sorted(l))
    for p in perms:
        if list(p) == l:
            try:
                return list(perms.__next__())
            except StopIteration:
                return sorted(l)
                # At the cost of allocating extra memory, we can
                # sort this input list only once.


if __name__ == '__main__':
    print(greater_perm([1, 2, 3]))
    print(greater_perm([3, 2, 1]))
