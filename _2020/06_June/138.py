"""
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢,
and a 1¢.
"""


def greedy(n: int) -> int:
    """Greedy method using division and modulo"""
    coins = [25, 10, 5, 1]
    total_coins = 0
    for coin in coins:
        total_coins += n // coin
        n = n % coin

    return total_coins


if __name__ == '__main__':
    assert greedy(16) == 3
    assert greedy(200) == 8
    assert greedy(1) == 1
