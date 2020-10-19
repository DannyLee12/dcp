"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers
smaller than N. The method is to take increasingly larger prime numbers, and
mark their multiples as composite.

For example, to find all primes less than 100, we would first mark
[4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three),
and so on. Once we have done this for all primes less than N, the unmarked
numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without
taking N as an input).
"""
from math import sqrt


def sieve(N: int) -> list:
    """Generate a list of primes < N"""
    sieve = set()
    for prime in range(2, int(sqrt(N))):
        if prime in sieve:
            continue  # Not a prime ;)
        val = prime * 2  # First occurrence is prime
        while val < N:
            sieve.add(val)
            val += prime

    return [x for x in range(2, N) if x not in sieve]


if __name__ == '__main__':
    print(sieve(10))
