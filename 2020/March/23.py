"""
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you
can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum
number of steps required to reach the end coordinate from the start. If there
is no possible path, then return null. You can move up, left, down, and right.
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum
number of steps required to reach the end is 7, since we would need to go
through (1, 2) because there is a wall everywhere else on the second row.

"""


def walkable(board, row, col):
    if row < 0 or row >= len(board):
        return False
    if col < 0 or col >= len(board[0]):
        return False
    return not board[row][col]


def get_walkable_neighbours(board, row, col):
    return [(r, c) for r, c in [
        (row, col - 1),
        (row - 1, col),
        (row + 1, col),
        (row, col + 1)]
        if walkable(board, r, c)
    ]


def bfs(board: list, start: tuple, end: tuple) -> int:
    """Only interested in the total length, excluding the starting node"""
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            for neighbour in get_walkable_neighbours(board, node[0], node[1]):
                new_path = path[:]
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == end:
                    return len(new_path) - 1
            visited.append(node)


if __name__ == '__main__':
    print(bfs([[False, False, False, False],
               [True, True, False, True],
               [False, False, False, False],
               [False, False, False, False]], (3, 0), (0, 0)))

