"""
Given an array of numbers representing the stock prices of a company in
chronological order and an integer k, return the maximum profit you can make
from k buys and sells. You must buy the stock before you can sell it, and you
must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""


def greedy(l: list, k: int) -> int:
    """Greedy solution"""
    hold = float("inf")
    profit = 0
    for x in l:
        if x <= hold:
            hold = x
        else:
            profit += x - hold
            k -= 1

    return profit


if __name__ == '__main__':
    assert greedy([5, 2, 4, 0, 1], 2) == 3
