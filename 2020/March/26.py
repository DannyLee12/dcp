"""
Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your
function should return true. The same regular expression on the string "raymond"
should return false.

Given the regular expression ".*at" and the string "chat", your function should
return true. The same regular expression on the string "chats" should return false.
"""
import re


def re_match(s: str, re: str) -> bool:
    """
    El Classico
    """
    if "." in re:
        return re.replace(".", "") in s


if __name__ == '__main__':
    assert re_match("ray", "ra.") is True
    assert re_match("raymond", "ra.") is False

