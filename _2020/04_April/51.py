"""
Given a function that generates perfectly random numbers between 1 and k
(inclusive), where k is an input, write a function that shuffles a deck of
cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""

from random import randint
from itertools import permutations


def shuffle(l: list) -> list:
    """Return a shuffled list - all permutations should be equally likely"""
    n = len(l)
    for i in range(n):
        s = randint(i, n - 1)
        l[s], l[i] = l[i], l[s]

    return l


if __name__ == '__main__':
    a = []
    for x in range(100):
        a.append(shuffle([1, 2]))

    print(a.count([1, 2]))
    print(a.count([2, 1]))

    b = []
    for y in range(100000):
        b.append(shuffle([1, 2, 3]))

    for perm in permutations([1, 2, 3]):
        print(b.count(list(perm))/1000)
