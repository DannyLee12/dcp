"""
The ancient Egyptians used to express fractions as a sum of several terms where
each numerator is one. For example, 4 / 13 can be represented
as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an
Egyptian fraction.
"""


def egyption_fractions(f: str) -> str:
    """Return a fraction as an egyption fraction"""
    # Assume first term < 10, 2nd term < 100 ...
    e = 0.000001
    for t in range(1, 10):
        for h in range(10, 100):
            for th in range(100, 1000):
                if abs(eval(f) - (1/t + 1/h + 1/th)) < e:
                    return f"1/{t} + 1/{h} + 1/{th}"


if __name__ == '__main__':
    print(egyption_fractions("4/13"))
