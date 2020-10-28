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
    f = eval(f)
    counter = 0
    i = ["0"]

    while abs(f - sum(eval(x) for x in i)) > e:
        c = counter * 10 + 1
        while 1/c + sum(eval(x) for x in i) > f:
            c += 1
        i.append(f"1/{c}")
        counter += 1

    return " + ".join(i[1:])


if __name__ == '__main__':
    print(egyption_fractions("4/13"))
