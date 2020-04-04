"""
Given a string, find the longest palindromic contiguous substring. If there are
more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The
longest palindromic substring of "bananas" is "anana".
"""


def is_palindrome(s: str) -> bool:
    """Return if the string is a palindrome"""
    return s == s[::-1]


def pal(s: str, current: str=None) -> str:
    """
    Return the longest palindrome in a string
    """
    if not current:
        current = s[0]
    n = len(s)
    m = len(current)

    if n <= m:
        return current

    for x in range(n):
        if n - x < m:
            break
        if is_palindrome(s[:n - x]):
            current = s[:n - x]

    return pal(s[1:], current)


if __name__ == '__main__':
    print(pal("banana"))
    print(pal("aabcdcb"))
