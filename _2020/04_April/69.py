"""
Given a list of integers, return the largest product that can be made by
multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since
that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


def largest_product(l: list) -> int:
    """Return the largest product of three integers"""
    l.sort()
    # Note there is an O(N) way of getting these max and min
    # values, but it is tedious. sorting in O(NlogN)
    return max((l[0] * l[1] * l[-1]), (l[-3] * l[-2] * l[-1]))


if __name__ == '__main__':
    print(largest_product([-10, -10, 5, 2]))
