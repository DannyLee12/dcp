"""
This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. That is, a 2D array
where the value at the i-th row and j-th column is (i + 1) * (j + 1)
(if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X
appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the
multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
"""

from random import randint


def mul_table(N: int, X: int) -> int:
    """Return the number of times X is in the table"""
    total = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j == X:
                total += 1

    return total


def mul_table_2(N: int, X:int) -> int:
    """Try again in O(N)"""
    total = 0
    for i in range(1, N+1):
        if X % i == 0 and X / i <= N:
            total += 1

    return total


if __name__ == '__main__':
    assert mul_table(6, 12) == mul_table(6, 12)
    int1, int2 = randint(1, 1000), randint(1, 2000)
    assert mul_table(int1, int2) == mul_table_2(int1, int2)
    print(mul_table(int1, int2))
    print(int1, int2)