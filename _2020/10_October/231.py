"""
Given a string with repeated characters, rearrange the string so that no two
adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return
None.
"""


def rearrange(s: str) -> str:
    """Rearrange a string so that no adjacent letters are the same"""
    ns = s[0]
    s = s[1:]

    while s:
        ns_letter = ns[-1]
        found = False
        for i, l in enumerate(s):
            if l != ns_letter:
                ns += l
                # Remove the letter from s
                s = s[:i] + s[i+1:]
                found = True
                break
        # If no other letter is found
        if not found:
            return None

    return ns


if __name__ == '__main__':
    assert rearrange("aaabbc") == "ababac"
    assert rearrange("aaab") is None
