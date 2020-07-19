"""
You are given n numbers as well as n probabilities that sum up to 1. Write a
function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2,
0.2], your function should return 1 10% of the time, 2 50% of the time, and 3
and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""
from random import random
from collections import defaultdict


def produce_numbers(nums: list, probs: list) -> int:
    """Return a number from nums"""
    val = 0
    r = random()
    for n, p in zip(nums, probs):
        # Check that val is in the range val -> val + prob
        if val <= r < val + p:
            return n
        val += p


if __name__ == '__main__':
    d = defaultdict(int)
    probs = [0.1, 0.5, 0.2, 0.2]
    for _ in range(100000):
        val = produce_numbers([1, 2, 3, 4], probs)
        d[val] += 1

    index = 1
    for p in probs:
        assert round(d[index] / 10000) == p * 10
        index += 1
