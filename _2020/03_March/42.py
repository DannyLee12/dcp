"""
Given a list of integers S and a target number k, write a function that returns
a subset of S that adds up to k. If such a subset cannot be made, then return
null.

Integers can appear more than once in the list. You may assume all numbers in
the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1]
since it sums up to 24.
"""


def subset(l: list, value: int, total: int = 0, sub: list = None) -> list:
    """Return the subset that adds up to k, assuming a sorted array"""
    if not sub:
        sub = []
    if not l:
        return None
    if l[0] + total == value:
        return sub + [l[0]]
    elif l[0] + total < value:
        sub.append(l[0])
        total += l[0]

    return subset(l[1:], value, total, sub)


def subset_sum(nums, k):
    A = [[None for _ in range(k + 1)] for _ in range(len(nums) + 1)]

    for i in range(len(nums) + 1):
        A[i][0] = []

    for i in range(1, len(nums) + 1):
        for j in range(1, k + 1):
            last = nums[i - 1]
            if last > j:
                A[i][j] = A[i - 1][j]
            else:
                if A[i - 1][j] is not None:
                    A[i][j] = A[i - 1][j]
                elif A[i - 1][j - last] is not None:
                    A[i][j] = A[i - 1][j - last] + [last]
                else:
                    A[i][j] = None

    return A[-1][-1]


if __name__ == '__main__':
    sorted_list = sorted([61, 12, 9, 5, 2, 1])[::-1]
    s_l = [6, 2, 1]
    print(subset(sorted_list, 24))
    print(subset(s_l, 10))
