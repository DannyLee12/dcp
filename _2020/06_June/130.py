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
            if not k:
                break

    return profit


def largest_profits(l: list, k:  int) -> int:
    """Always return the greatest profit, run k times"""
    total_profit = 0
    while k:
        n = len(l)
        largest_profit = 0
        large_i = -1
        large_j = -1
        for i in range(n):
            for j in range(i, n):
                if l[j] - l[i] > largest_profit:
                    large_j = j
                    large_i = i
                    largest_profit = l[j] - l[i]
        k -= 1
        l.pop(large_i)
        l.pop(large_j - 1)  # Lose one position due to above pop
        total_profit += largest_profit

    return total_profit


if __name__ == '__main__':
    assert greedy([5, 2, 4, 0, 1], 2) == 3
    # assert largest_profits([5, 2, 4, 0, 1], 2) == 3
    print(greedy([5, 0, 1, 2, 4], 1))  # 1, should be 4 Buy 0 sell 4
    assert largest_profits([5, 0, 1, 2, 4], 1) == 4
