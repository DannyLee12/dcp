"""
You have n fair coins and you flip them all at the same time. Any that come up
tails you set aside. The ones that come up heads you flip again. How many
rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to
play until one coin remains.
"""
from random import random
from math import log


def flip_coins(n: int, count: int = 0) -> int:
    """How many times do you need to flip coins until only one remains"""
    heads = 0
    for _ in range(n):
        if random() > 0.5:
            heads += 1
    if heads <= 1:
        return count

    return flip_coins(heads, count + 1)


def coins(n):
    return log(n, 2)


if __name__ == '__main__':
    print(flip_coins(100))
    print(flip_coins(10))
    print(flip_coins(1))
    print(coins(100))
    print(coins(10))
    print(coins(1))
