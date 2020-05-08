"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""


def sum_digits(n: int):
    total = 0
    for c in str(n):
        total += int(c)

    return total


def perfect_number(n: int) -> int:
    """Return the nth perfect number"""
    # return (10 * n) + (10 * ((n // 10) + 1)) - n - (n // 10)
    count = 0
    for i in range(n * 100):
        if sum_digits(i) == 10:
            count += 1
        if count == n:
            return i


if __name__ == '__main__':
    assert perfect_number(2) == 28
