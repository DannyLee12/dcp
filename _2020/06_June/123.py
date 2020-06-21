"""
Given a string, return whether it represents a number. Here are the different
kinds of numbers:

    "10", a positive integer
    "-10", a negative integer
    "10.1", a positive real number
    "-10.1", a negative real number
    "1e5", a number in scientific notation

And here are examples of non-numbers:

    "a"
    "x 1"
    "a -2"
    "-"
"""


def check_number(s: str) -> int:
    """Check if a number is a string"""
    try:
        int(s)
        return True
    except ValueError:
        try:
            float(s)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    assert check_number("10")
    assert check_number("-10")
    assert check_number("10.1")
    assert check_number("-10.1")
    assert check_number("1e5")
    assert not check_number("a")
    assert not check_number("x 1")
    assert not check_number("a -2")
    assert not check_number("-")
