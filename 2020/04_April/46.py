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
    SUPERCEEDED by pal2
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


def pal2(s: str) -> str:
    """Return the longest substring in O(len(s))"""
    # Consider Odd case
    longest = s[0]
    n = len(s)
    for i, letter in enumerate(s):
        x = 1
        y = 0
        try:
            while s[i - x] == s[i + x]:
                if i - x < 0 or i + x >= n:
                    break
                candidate = s[i - x:i + x + 1]
                if len(candidate) > len(longest):
                    longest = candidate
                x += 1
            while s[i - y] == s[i + y - 1]:
                if i - y < 0 or i + y - 1 >= n:
                    break
                candidate2 = s[i - y:i + y]
                if len(candidate2) > len(longest):
                    longest = candidate2
                y += 1
        except IndexError:
            pass


    return longest

if __name__ == '__main__':
    # print(pal("banana"))
    # print(pal("aabcdcb"))
    print(pal2("banana"))
    print(pal2("aabcdcb"))
    print(pal2("banna"))
