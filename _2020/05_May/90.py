"""
Given an integer n and a list of integers l, write a function that randomly
generates a number from 0 to n-1 that isn't in l (uniform).
"""
from random import randint, choice


def gen_random(n: int, l: list) -> int:
    """Randomly generate a number from 0 to n-1 that is not in l"""
    s = set(l)
    i = randint(0, n - 1)
    if i in s:
        return gen_random(n, l)

    return i


def gen_random_improved(n: int, l: list) -> int:
    """Randomly generate a number from 0 to n-1 that is not in l"""
    r = set([x for x in range(n-1)]) - set(l)

    return choice(list(r))


if __name__ == '__main__':
    assert gen_random(5, [2, 3]) in [0, 1, 4]
    for _ in range(100):
        assert gen_random_improved(5, [2, 3]) in [0, 1, 4]
