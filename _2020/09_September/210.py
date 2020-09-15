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


def collatz(n: int, count: int=0):
    if n == 1:
        return count
    if n % 2 == 0:
        return collatz(n // 2, count + 1)
    else:
        return collatz(3*n + 1, count + 1)


if __name__ == '__main__':
    max_val = 0
    for x in range(1, 1_000_00):
        iterations = collatz(x)
        if iterations > max_val:
            print(x)
            max_val = iterations
