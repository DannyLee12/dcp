"""
Given a string of parentheses, write a function to compute the minimum number
of parentheses to be removed to make the string valid (i.e. each open
parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string
")(", you should return 2, since we must remove all of them.
"""


def pop_parentheses(s: str) -> int:
    """How many parentheses should be removed to balance the string"""
    count = 0
    for c in s:
        if c == "(":
            count += 1
        elif c == ")":
            count -= 1

    return abs(count)


if __name__ == '__main__':
    assert pop_parentheses("()())()") == 1
    assert pop_parentheses("(()") == 1
    assert pop_parentheses("((()") == 2
    assert pop_parentheses("(()))") == 1
    assert pop_parentheses("()))))") == 4

