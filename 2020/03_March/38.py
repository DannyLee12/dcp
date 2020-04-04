"""
You have an N by N board. Write a function that, given N, returns the number of
possible arrangements of the board where N queens can be placed on the board
without threatening each other, i.e. no two queens share the same row, column,
or diagonal.
"""


def under_attack(board: list, i: int, j: int, N: int):
    """Return True if the block is under attack"""
    # Check rows and columns
    for x in range(N):
        if board[i][x] == 1 or board[x][j] == 1:
            return True
    # Check diagonals
    for y in range(N):
        for z in range(N):
            if (y + z == i + j) or (y - z == i - j):
                if board[y][z] == 1:
                    return True
    return False


def n_queens(n: int, board: list):
    """Recursively solve for n queens"""
    if n == 0:
        return True

    for a in range(N):
        for b in range(N):
            if not under_attack(board, a, b, N) and board[a][b] != 1:
                board[a][b] = 1
                if n_queens(n-1, board):
                    return True
                board[a][b] = 0


if __name__ == '__main__':
    N = 8
    total = 0
    for x in range(N):
        board = [[0] * N for _ in range(N)]
        board[0][x] = 1
        if n_queens(N-1, board):
            total += 1

    print(total)
