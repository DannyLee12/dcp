"""
You are given a 2-d matrix where each cell represents number of coins in that
cell. Assuming we start at matrix[0][0], and can only move right or down,
find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""


def max_coins(l: list) -> int:
    """Return the maximal number of coins that can be returned"""
    n = len(l)
    m = len(l[0])

    def dfs(x, y, l):
        if x == n - 1 and y == m - 1:
            return l[x][y]
        if x+1 < n and y + 1 < m:
            return max(l[x][y] + dfs(x+1, y, l), l[x][y] + dfs(x, y+1, l))
        elif x+1 < n:
            return l[x][y] + dfs(x+1, y, l)
        elif y+1 < m:
            return l[x][y] + dfs(x, y+1, l)

    return dfs(0, 0, l)


if __name__ == '__main__':
    l = [[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]]
    assert max_coins(l) == 12
