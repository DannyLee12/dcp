"""
The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""


def distance(s1, s2):
    x = len(s1) + 1
    y = len(s2) + 1

    A = [[-1 for i in range(x)] for j in range(y)]

    for i in range(x):
        A[0][i] = i

    for j in range(y):
        A[j][0] = j

    for i in range(1, y):
        for j in range(1, x):
            if s1[j - 1] == s2[i - 1]:
                A[i][j] = A[i - 1][j - 1]
            else:
                A[i][j] = min(
                    A[i - 1][j] + 1,
                    A[i][j - 1] + 1,
                    A[i - 1][j - 1] + 1
                )

    print(A)
    print(A[y - 1][x - 1])


if __name__ == '__main__':
    assert distance("kitten", "sitting") == 3
