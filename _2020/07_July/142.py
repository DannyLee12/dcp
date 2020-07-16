"""
This problem was asked by Google.

You're given a string consisting solely of (, ), and *. * can represent either
a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""


def is_balanced(s: str, b=0) -> bool:
    """Return whether a string of parentheses is balanced"""
    for i, c in enumerate(s):
        if c == '(':
            b += 1
        elif c == ')':
            b -= 1
            if b < 0:
                return False
        elif c == '*':
            if is_balanced('(' + s[i + 1:], b):
                return True
            elif is_balanced(')' + s[i + 1:], b):
                return True
            elif is_balanced(s[i + 1:], b):
                return True

    return not b


if __name__ == '__main__':
    assert is_balanced("(()*")
    assert is_balanced("(*)")
    assert not is_balanced(")*(")

    assert is_balanced("(**********)")
    assert is_balanced("(*)*()*)()*)(*)())*)")
    assert not is_balanced("((((((((((*********")
