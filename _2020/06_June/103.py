"""
Given a string and a set of characters, return the shortest substring
containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i},
you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""
from collections import defaultdict


def shortest_substring(s: str, vals: set) -> str:
    """Return the shortest substring containing all s"""
    n = len(s)
    d = defaultdict(int)
    for i, c in enumerate(s):
        s2 = vals.copy()
        for x in range(i, n):
            if s[x] in s2:
                s2 -= {s[x]}
            d[i] += 1
        if s2:
            del d[i]

    result = min(d.items(), key=lambda x: x[1])

    return s[result[0]:result[0] + result[1]]


if __name__ == '__main__':
    print(shortest_substring("figehaeci", {"a", "e", "i"}))
