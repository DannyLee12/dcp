"""
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exists(board, "ABCCED") returns true,
exists(board, "SEE") returns true,
exists(board, "ABCB") returns false.
"""


def exists(grid: list, word: str) -> bool:
    """
    Return true is the word is in the grid
    """
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs(x, y, word, visited=None):
        if visited is None:
            visited = []
        for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (x+a, y+b) not in visited:
                visited.append((x+a, y+b))
                if 0 <= x + a < n and 0 <= y + b < m:
                    if grid[x+a][y+b] == word[0]:
                        if len(word) == 1:
                            return True
                        if dfs(x+a, y+b, word[1:], visited):
                            return True
        return False

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if not visited[i][j]:
                if cell == word[0]:
                    if dfs(i, j, word[1:]):
                        return True
                visited[i][j] = True

    return False


if __name__ == '__main__':
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    assert exists(board, "ABCCED") is True
    assert exists(board, "SEE") is True
    assert exists(board, "ABCB") is False
