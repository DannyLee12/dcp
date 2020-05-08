"""
This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a
probability that's not 50-50 (but also not 0-100 or 100-0). You do not know
the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

from random import randint


def toss_biased():
    r = randint(0, 1000)

    return r < 200


def toss_non_biased():
    """Return a non-biased result"""
    a = toss_biased()
    b = toss_biased()
    if a is True and b is False:
        return True
    if a is False and b is True:
        return False

    return toss_non_biased()


if __name__ == '__main__':
    total = 0
    total_non_biased = 0
    for x in range(10000):
        if toss_biased():
            total += 1
        if toss_non_biased():
            total_non_biased += 1

    print(total/10000)
    print(total_non_biased/10000)
