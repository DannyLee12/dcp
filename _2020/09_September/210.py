"""
This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any
positive integer:

    if n is even, the next number in the sequence is n / 2
    if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1.
Test this conjecture.

Bonus: What input n <= 1_000_000 gives the longest sequence?

"""

lengths = {}


def collatz(n: int):
    if n not in lengths:
        if n == 1:
            lengths[n] = 1
        if n % 2 == 0:
            lengths[n] = 1 + collatz(n // 2)
        else:
            lengths[n] = 1 + collatz(3*n + 1)

    return lengths[n]


if __name__ == '__main__':
    max_val = 0
    for x in range(1, 1_000_000):
        iterations = collatz(x)
        if iterations > max_val:
            print(x)
            max_val = iterations
