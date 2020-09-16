"""
Given a string and a pattern, find the starting indices of all occurrences of
the pattern in the string. For example, given the string "abracadabra" and the
pattern "abr", you should return [0, 7].
"""


def naive(s: str, pattern: str) -> list:
    """Return the starting indexes of all patterns in s"""
    n = len(pattern)
    sn = len(s)
    l = []
    for i, c in enumerate(s):
        j = 0
        while s[j+i] == pattern[j] and j < n - 1 and j+i < sn - 1:
            j += 1
            if j == n - 1:
                l.append(i)
                break

    return l


if __name__ == '__main__':
    print(naive("abracadabra", "abr"))
