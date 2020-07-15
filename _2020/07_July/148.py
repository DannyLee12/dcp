"""
Gray code is a binary code where each successive value differ in only one bit,
as well as when wrapping around. Gray code is common in hardware so that we
don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""


def gray(n: int) -> list:
    """Return gray codes"""
    if n == 1:
        return [[0], [1]]
    else:
        return [[0] + x for x in gray(n-1)] + [[1] + x for x in reversed(gray(n-1))]


if __name__ == '__main__':
    print(gray(2))
    print(gray(3))
    print(gray(4))
