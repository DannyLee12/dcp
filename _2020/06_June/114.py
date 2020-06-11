"""
Given a string and a set of delimiters, reverse the words in the string while
maintaining the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/"
, "hello//world:here"
"""


def reverse_words(s: str, delims: list) -> str:
    """Reverse the words in a string"""
    words = []
    d = []
    start = 0
    for i, c in enumerate(s):
        if c in delims:
            words.append(s[start:i])
            start = i + 1
            d.append(c)
    words.append(s[start:])

    reversed_words = reversed(words)
    delims = iter(d)
    s2 = ""
    while True:
        try:
            w = next(reversed_words)
            if w == "":
                continue
        except StopIteration:
            w = ""
        try:
            de = next(delims)
        except StopIteration:
            de = ""
        s2 += w + de
        if not w and not de:
            break

    return s2


if __name__ == '__main__':
    print(reverse_words("hello/world:here", ['/', ':']))
    print(reverse_words("hello/world:here/", ['/', ':']))
    print(reverse_words("hello//world:here", ['/', ':']))
