"""
Given a word W and a string S, find all starting indices in S which are
anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

from itertools import permutations


def find_anagrams(w: str, s: str) -> tuple:
    """Return positions of all anagrams of w in s"""
    positions = ()
    n = len (w)
    for perm in permutations(w):
        st = 0
        while st < n:
            try:
                ind = s.index("".join(perm), st)
            except ValueError:
                break
            if ind != -1:
                positions += (ind,)
                st = ind + 1
            else:
                break

    return positions


if __name__ == '__main__':
    assert find_anagrams("ab", "abxaba") == (0, 3, 4)
    assert find_anagrams("ab", "acaadf") == tuple()
