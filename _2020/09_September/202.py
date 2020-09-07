"""
Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
Do not convert the integer into a string.
"""
import math


def is_pal(i: int) -> bool:
    """Return true if i is a palindrome"""
    digits = int(math.log10(i)) + 1
    delta = 0
    if digits % 2 == 1:
        delta = 1  # In the case of a number with an odd length
                   # add a delta to move the mod one position

    def reverse_number(n):
        r = 0
        while n > 0:
            r *= 10
            r += n % 10
            n //= 10
        return r

    print(i // 10 ** (digits // 2))
    print(reverse_number(i % 10 ** ((digits // 2) + delta)))

    return i // 10 ** (digits // 2) == reverse_number(i % 10 ** ((digits // 2) + delta))


if __name__ == '__main__':
    assert is_pal(121)
    assert is_pal(888)
    assert not is_pal(678)
    assert is_pal(1122334444332211)
