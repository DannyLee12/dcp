"""
Conway's Game of Life takes place on an infinite two-dimensional board of
square cells. Each cell is either dead or alive, and at each tick, the
following rules apply:

    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.

A cell neighbours another cell if it is horizontally, vertically, or diagonally
adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a
starting list of live cell coordinates and the number of steps it should run for.
Once initialized, it should print out the board state at each step. Since it's
an infinite board, print out only the relevant coordinates, i.e. from the
top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot
(.).
"""
import copy


def fix_board(board: list):
    """Update the board to have enough rows and columns"""
    min_x, min_y = float("inf"), float("inf")
    max_x, max_y = 0, 0
    for x, row in enumerate(board):
        for y, k in enumerate(row):
            if board[x][y] == "*":
                min_x = min(x, min_x)
                max_x = max(x, max_x)
                min_y = min(y, min_y)
                max_y = max(y, max_y)

    n = len(board)
    m = len(board[0])

    if min_x == 0:
        board.insert(0, ["." for _ in range(m)])
    elif min_x == n - 1:
        del board[0]
    if max_x == n - 1:
        board.append(["." for _ in range(m)])
    elif max_x == n:
        del board[-1]
    if min_y == 0:
        for row in board:
            row.insert(0, ".")
    elif min_y == m - 1:
        for row in board:
            del row[0]
    if max_y == m - 1:
        for row in board:
            row.append(".")
    elif max_y == m:
        for row in board:
            del row[-1]


def gol(steps: int, board: list):
    """
    Game of life - runs for steps steps
    :param steps: Number of steps to run for
    """
    if steps == 0:
        return

    print_board(board)
    fix_board(board)
    b = copy.deepcopy(board)
    for x, row in enumerate(board):
        for y, k in enumerate(row):
            neighbours = get_neighbours(board, x, y)
            if board[x][y] == '.' and neighbours == 3:
                b[x][y] = '*'
            elif board[x][y] == "*":
                if neighbours < 2:
                    b[x][y] = "."
                elif neighbours in [2, 3]:
                    pass
                elif neighbours > 3:
                    b[x][y] = "."

    gol(steps - 1, b)


def get_neighbours(board: list, x: int, y: int):
    """Return the number of living neighbours of a given cell"""
    living = 0
    n = len(board)
    m = len(board[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j == 0 and i == 0:
                continue
            if 0 < x + i < n and 0 < y + j < m:
                if board[x+i][y+j] == "*":
                    living += 1

    return living


def print_board(board: list):
    """Print the board nicely"""
    p = ""
    for row in board:
        for x in row:
            p += x
        p += "\n"

    print(p)


if __name__ == '__main__':
    l = ['*', '*', '*']
    n = len(l)
    board = [["." for _ in range(n + 2)]] + [
        ['.'] + l + ['.']] + [
                ["." for _ in range(n + 2)]]
    gol(10, board)
