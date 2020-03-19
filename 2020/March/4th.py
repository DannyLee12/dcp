"""
This problem was asked by Facebook.
Given a stream of elements too large to store in memory, pick a random element
from the stream with uniform probability.
"""
import random


def random_stream(stream):
    """Recalculate the random value for each value in the stream"""
    for i, x in enumerate(stream):
        if i == 0:
            random_value = x
        elif random.randint(1, 1 + i) == 1:
            random_value = x
    return random_value


if __name__ == '__main__':
    print(random_stream([1, 2, 3, 4, 5]))
