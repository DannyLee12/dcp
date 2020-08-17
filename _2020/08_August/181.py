"""
Given a string, split it into as few strings as possible such that each string
is a palindrome.

For example, given the input string racecarannakayak, return ["racecar",
"anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].
"""


def is_pal(s: str) -> bool:
    """Return True if the string is a palindrome"""
    return s == s[::-1]


def split_string(s: str) -> list:
    """Split a string into a minimum number of palindromes"""
    if not s:
        return []
    n = len(s)
    for i in range(n, 0, -1):
        if is_pal(s[:i]):
            return [s[:i]] + split_string(s[i:])


if __name__ == '__main__':
    assert split_string("racecarannakayak") == ["racecar", "anna", "kayak"]
    assert split_string("abc") == ["a", "b", "c"]
