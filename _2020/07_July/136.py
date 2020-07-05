"""
Given an N by M matrix consisting only of 1's and 0's, find the largest
rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]

Return 4.
"""

DIRS = ((-1, 0),
        (0, -1), (0, 1),
        (1, 0))


def max_area(l: list) -> int:
    """Return the largest rectangle of 1s"""
    m = len(l)
    n = len(l[0])

    def bfs(x, y, down, right):
        total = 0
        queue = [(x, y)]
        visited = []

        downlimit, rightlimit = find_limits(down, right, x, y)

        while queue:
            x, y = queue.pop(0)
            if (x, y) not in visited:
                visited.append((x, y))
                if l[y][x]:
                    total += 1

            if down:
                if y + 1 < downlimit:
                    queue.append((x, y + 1))
            if right:
                if x + 1 < rightlimit:
                    queue.append((x + 1, y))

        return total

    def find_limits(down, right, x, y):
        # Find limits
        downlimit = y
        r, d = x, y
        if down:
            while l[d][x] == 1:
                downlimit += 1
                if d == m - 1:
                    break
                d += 1
        rightlimit = x
        if right:
            while l[y][r] == 1:
                rightlimit += 1
                if r == n - 1:
                    break
                r += 1
        return downlimit, rightlimit

    max_area = 0

    for a, row in enumerate(l):
        for b, col in enumerate(row):
            if col:
                # Possible directions
                down, right = 0, 0
                if a + 1 < m:
                    down = l[a+1][b]
                if b + 1 < n:
                    right = l[a][b+1]
                max_area = max(max_area, bfs(b, a, down, right))

    return max_area


if __name__ == '__main__':
    l = [[1, 0, 0, 0],
         [1, 0, 1, 1],
         [1, 0, 1, 1],
         [0, 1, 0, 0]]

    l2 = [[1, 0, 0, 0, 1],
          [1, 0, 1, 1, 1],
          [1, 0, 1, 1, 1],
          [0, 1, 0, 0, 1]]

    assert max_area(l) == 4
    assert max_area(l2) == 6
