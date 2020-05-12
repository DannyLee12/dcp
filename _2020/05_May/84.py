"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, so an island is a group of 1s
that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1

"""


def check_land(l: list, x: int, y: int, visited: list) -> (int, int):
    """Return the position of any land that hasn't been visited or None"""
    for a in range(-1, 2):
        for b in range(-1, 2):
            if a == b == 0:
                continue
            if 0 <= x+a < len(l) and 0 <= y+b < len(l[0]):
                if not visited[x+a][y+b]:
                    visited[x+a][y+b] = True
                    if l[x+a][y+b] == "1":
                        visited = check_land(l, x+a, y+b, visited)

    return visited


def count_islands(l: list) -> int:
    """Return the number of islands"""
    n = len(l)
    m = len(l[0])
    total = 0
    visited = [[False for _ in range(m)] for __ in range(n)]
    for i, row in enumerate(l):
        for j, element in enumerate(row):
            if element == "1" and not visited[i][j]:
                total += 1
                visited = check_land(l, i, j, visited)

    return total


if __name__ == '__main__':
    l = [x.split() for x in """1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1""".split("\n")]
    assert count_islands(l) == 4