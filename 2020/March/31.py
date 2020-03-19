"""
The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""


def edit_distance(s1: str, s2: str) -> int:
    total = 0
    for x, y in zip(s1, s2):
        if x != y:
            total += 1

    return total + abs(len(s1) - len(s2))


if __name__ == '__main__':
    assert edit_distance("kitten", "sitting") == 3
