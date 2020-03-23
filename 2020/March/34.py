"""
This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest
number of characters as possible anywhere in the word. If there is more than
one palindrome of minimum length that can be made, return the lexicographically
earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can
add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three
letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""


def is_pal(s: str) -> bool:
    """Is the string a pallindrome"""
    return s == s[::-1]


def find_pal_head(s: str, orig: str = None) -> str:
    """
    Add the fewest number of chars to make the word a
    palindrome
    """
    if not orig:
        orig = s
    # Recursively find the longest palindrome, then return the letters needed
    if is_pal(s):
        new_str = orig.replace(s, "")
        return new_str[::-1] + s + new_str
    else:
        return find_pal_head(s[:-1], orig)


def find_pal_tail(s: str, orig: str = None) -> str:
    """
    Similar to find_pal_head, but with a different resursion pattern
    :param s:
    :param orig:
    :return:
    """
    if not orig:
        orig = s
    # Recursively find the longest palindrome, then return the letters needed
    if is_pal(s):
        new_str = orig.replace(s, "")
        return new_str[::-1] + s + new_str
    else:
        return find_pal_tail(s[1:], orig)


def find_pal(s: str) -> str:
    """
    Call both head and tail methods to get shortest option
    :param s:
    :return:
    """
    head = find_pal_head(s)
    tail = find_pal_tail(s)
    if len(head) <= len(tail):
        return head
    return tail


if __name__ == '__main__':
    print(find_pal("race"))
    print(find_pal("google"))
    print(find_pal("lgoog"))
    print(find_pal("racecar"))