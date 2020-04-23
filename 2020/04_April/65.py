"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12

"""


def print_clockwise(l: list) -> None:
    """
    Print out numbers in a spiral
    """
    def right(l):
        while l[0]:
            print(l[0].pop(0))
        del l[0]

    def down(l):
        for row in l:
            print(row.pop())

    def left(l):
        while l[-1]:
            print(l[-1].pop())
        del l[-1]

    def up(l):
        length = len(l)
        for i, row in enumerate(l):
            print(l[length - i - 1].pop(0))

    while l:
        right(l)
        down(l)
        left(l)
        up(l)


if __name__ == '__main__':
    print_clockwise([[1,  2,  3,  4,  5],
                     [6,  7,  8,  9,  10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20]])
