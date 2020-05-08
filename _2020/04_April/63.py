"""
Given a 2D matrix of characters and a target word, write a function that
returns whether the word can be found in the matrix by going left-to-right,
or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost
column. Similarly, given the target word 'MASS', you should return true,
since it's the last row.
"""


def wordsearch(l: list, word: str) -> bool:
    """Return whether the word is in the grid"""
    def find_word(x, y, word, l):
        n = len(l)
        if not word:
            return True
        if x+1 < n and l[x+1][y] == word[0]:
            return find_word(x+1, y, word[1:], l)
        elif y+1 < n and l[x][y+1] == word[0]:
            return find_word(x, y+1, word[1:], l)
        else:
            return False

    for i, row in enumerate(l):
        for j, letter in enumerate(row):
            if letter == word[0]:
                if find_word(i, j, word[1:], l):
                    return True

    return False


if __name__ == '__main__':
    print(wordsearch([['F', 'A', 'C', 'I'],
                      ['O', 'B', 'Q', 'P'],
                      ['A', 'N', 'O', 'B'],
                      ['M', 'A', 'S', 'S']], "FOAM"))
    print(wordsearch([['F', 'A', 'C', 'I'],
                      ['O', 'B', 'Q', 'P'],
                      ['A', 'N', 'O', 'B'],
                      ['M', 'A', 'S', 'S']], "MASS"))
    print(wordsearch([['F', 'A', 'C', 'I'],
                      ['O', 'B', 'Q', 'P'],
                      ['A', 'N', 'O', 'B'],
                      ['M', 'A', 'S', 'S']], "IPBS"))
