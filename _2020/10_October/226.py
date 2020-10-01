"""
You come across a dictionary of sorted words in a language you've never seen
before. Write a program that returns the correct order of letters in this
language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return
['x', 'z', 'w', 'y'].
"""
from collections import defaultdict


def order_letters(l: list) -> list:
    """Return the order of letters given a sorted list"""
    wordlist = []
    wl = []
    i = 0
    while i < len(l) - 1:
        j = 0
        while l[i][j] == l[i+1][j]:
            j += 1
        wordlist.append(f"{l[i][j]}{l[i+1][j]}")
        i += 1

    wl = [wordlist[0]]
    scores = {wl[0][0]: 0}
    dd = defaultdict(int)
    for k, word in enumerate(wordlist):
        if word[0] in scores:
            scores[word[1]] = scores[word[0]] + 1
        if word[1] in scores:
            scores[word[0]] = scores[word[1]] - 1
            scores[word[1]] = scores[word[1]] + 2

    return [x[0] for x in sorted(scores.items(), key=lambda x: x[1])]


if __name__ == '__main__':
    assert order_letters(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']) == ["x", "z", "w", "y"]
