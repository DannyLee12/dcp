"""
This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will
be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4

If there are more than one solution possible, return the lexicographically
smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with
c <= d, then

[a, b] < [c, d]

If a < c OR a==c AND b < d.
"""


def sieve(n: int) -> set:
    """Return a list of primes up to n"""
    s = set()
    for i in range(2, n // 2 + 1):
        while i < n:
            i *= 2
            if i not in s:
                s.add(i)

    values = set(j for j in range(2, n))

    return values - s


def goldbachs(n: int) -> (int, int):
    """Return two primes that equal n"""
    if n % 2 != 0:
        raise ValueError("Value is not even")
    primes = sieve(n - 1)
    for prime in primes:
        if n - prime in primes:
            return prime, n - prime


if __name__ == '__main__':
    assert goldbachs(4) == (2, 2)
    print(goldbachs(466))
    print(goldbachs(100234))
    assert goldbachs(6) == (3, 3)
