"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a
Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

from random import random
import math


def monte_carlo(iterations: int) -> float:
    """
    Basically, we need to create random numbers and see whether they are
    inside or outside the circle with radius r in the square of side r
    Explanation:
        Ratio of the areas is pi/4
        This is shown by:
            Area of the large square is 4 * r2
            Area of the circle is pi * r2
            Therefore Area(large_circle)/Area(circle) = 4/pi
            Therefore, finally:
                pi = 4 * in_circle/Total square
    :return: pi approximation
    """
    # Create a random x, y point between 0 and 1
    in_circle = 0
    for _ in range(iterations):
        x, y = random(), random()
        if math.hypot(x, y) < 1:
            in_circle += 1

    return 4 * in_circle / iterations


if __name__ == '__main__':
    print(monte_carlo(999_999))
