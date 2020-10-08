"""
Implement the function fib(n), which returns the nth number in the Fibonacci
sequence, using only O(1) space.
"""


def fib(n):
    """Return the nth fibonacci number using 0(1) space"""
    if n == 1 or n == 0:
        return 1

    temp1, temp2 = 1, 1
    counter = 0

    while counter < n - 1:
        val = temp1 + temp2
        temp1 = temp2
        temp2 = val
        counter += 1

    return val


if __name__ == '__main__':
    for i in range(10):
        print(fib(i))
