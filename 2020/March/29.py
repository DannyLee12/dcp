"""
Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
"""


def encode(s: str) -> str:
    """
    Return encoded string
    AAAABBBCCDAA -> 4A3B2C1D2A
    """
    n = len(s)
    r_str = ""
    prev = None
    total = 0
    for i in s:
        if not prev:
            pass
        elif prev != i:
            r_str += str(total + 1)
            r_str += prev
            total = 0
        elif prev == i:
            total += 1
        prev = i

    r_str += str(total + 1)
    r_str += prev

    return r_str


if __name__ == '__main__':
    print(encode("AAAAABBBBCCC"))
    print(encode("ABC"))
    print(encode("AABBCC"))
