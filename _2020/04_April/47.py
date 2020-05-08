"""
Given a array of numbers representing the stock prices of a company in
chronological order, write a function that calculates the maximum profit you
could have made from buying and selling that stock once. You must buy before
you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could
buy the stock at 5 dollars and sell it at 10 dollars.
"""


def stocks(l: list) -> int:
    """Return the max profit"""
    m = float("inf")
    profit = float("-inf")
    for x in l:
        m = min(x, m)
        profit = max(profit, x - m)

    return profit


if __name__ == '__main__':
    print(stocks([9, 11, 8, 5, 7, 10]))
    print(stocks([9, 11, 8, 3, 7, 10]))
    print(stocks([9, 11, 8, 5, 7, 10, 12]))
