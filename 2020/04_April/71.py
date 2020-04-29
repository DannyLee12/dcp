"""
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with
uniform probability, implement a function rand5() that returns an integer from
1 to 5 (inclusive).
"""

from random import randint
from collections import defaultdict


def rand7():
    return randint(1, 7)


def rand5():
    """Return an integer from 1 - 5 inclusive"""
    n = rand7()
    if n == 1 or n == 7:
       return rand5()

    return n - 1


if __name__ == '__main__':
    d = defaultdict(int)
    for _ in range(50000):
        d[rand5()] += 1

    print(d)