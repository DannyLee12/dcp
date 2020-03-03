"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def two_options(l: list) -> int:
    """
    The idea here is that there are two options, one that starts at index 0
    and one that starts at index 1. Then we only need to consider the event
    if it makes the total larger.
    """
    n = len(l)
    last_used = None
    total = 0
    lu = None
    total2 = 0
    for x in range(n):
        y = x + 1 if x + 1 < n else x
        if last_used is None:
            if total + l[x] > total:
                total += l[x]
                last_used = x
        else:
            if total + l[x] > total and last_used != x - 1:
                total += l[x]
                last_used = x

        if lu is None:
            if total2 + l[y] > total2:
                total2 += l[y]
                lu = y
        else:
            if total2 + l[y] > total2 and lu != y - 1:
                total2 += l[y]
                lu = y

    if total > total2:
        return total

    return total2


def rec(l: list, start: int=0) -> int:
    """
    Consider a recursive strategy - working for this case
    Time complexity seems alright actually?
    Space Complexity TBC
    """
    if len(l) == 1:
        return l[0]
    # Start at 0:
    if len(l) == 2:
        if l[0] > l[1]:
            return l[0]
        else:
            return l[1]
    return l[start] + rec(l[start + 2:])


if __name__ == '__main__':
    print(rec([2, 4, 6, 2, 5]))
    print(rec([2, 4, 6, 2, 5], 1))
    print(rec([5, 1, 1, 5]))
    print(rec([5, 1, 1, 5, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))