"""
Given a word W and a string S, find all starting indices in S which are
anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""

from itertools import permutations
import time


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


def find_anagrams_fast(w: str, s: str) -> tuple:
    """Return positions of all anagrams of w in s, but fast"""
    positions = tuple()
    n = len(w)
    sw = sorted(w)  # Lexicographically sort w
    for i in range(len(s) - n + 1):
        if sorted(s[i:i+n]) == sw:
            positions += (i, )

    return positions


if __name__ == '__main__':
    assert find_anagrams("ab", "abxaba") == (0, 3, 4)
    assert find_anagrams("ab", "acaadf") == tuple()
    t1 = time.time()
    for _ in range(1000):
        find_anagrams("abcdefg", "abcdefgabcdefgabcdefgabcdefgabcdefg")
    print(f"Time taken = {time.time() - t1} seconds")

    assert find_anagrams_fast("ab", "abxaba") == (0, 3, 4)
    assert find_anagrams_fast("ab", "acaadf") == tuple()
    t2 = time.time()
    for _ in range(1000):
        find_anagrams_fast("abcdefg", "abcdefgabcdefgabcdefgabcdefgabcdefg")
    print(f"Time takes = {time.time() - t2} Seconds")
