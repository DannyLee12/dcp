"""
Given a multiset of integers, return whether it can be partitioned into two
subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return
true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which
both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't
 split it up into two subsets that add up to the same sum.
"""


def partition_l(l: list) -> bool:
    """Return whether the set can be split in two subsets of the same value"""
    l.sort()
    n = len(l)
    s1 = []
    while l:
        s1.append(l.pop())
        if sum(s1) == sum(l):
            print(s1, l)
            print(s1)
            return True

    return False


if __name__ == '__main__':
    # print(partition({15, 5, 20, 10, 35, 15, 10}))
    print(partition_l([15, 5, 20, 10, 35, 15, 10]))
    print(partition_l([15, 5, 20, 10, 35]))
