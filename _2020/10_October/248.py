"""
Find the maximum of two numbers without using any if-else statements,
branching, or direct comparisons.
"""


def compare(x: int, y: int) -> int:
    """Return the max of x and y"""
    while x and y:
        print(x & y)
        x -= 1
        y -= 1
        print(x, y)
        # break




if __name__ == '__main__':
    compare(10, 11)