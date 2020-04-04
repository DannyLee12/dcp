"""
Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def well_formed(s: str) -> bool:
    """Use a stack"""
    stack = []
    for c in s:
        if c in ["(", "{", "["]:
            stack.append(c)
        else:
            if c == '}' and stack[-1] != '{' or \
               c == ')' and stack[-1] != '(' or \
               c == ']' and stack[-1] != '[':
                return False

            stack.pop()

    return len(stack) == 0


if __name__ == '__main__':
    assert well_formed("([])[]({})") is True
    assert well_formed("([)]") is False
    assert well_formed("((()") is False
