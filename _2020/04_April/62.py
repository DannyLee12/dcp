"""
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count
the number of ways of starting at the top-left corner and getting to the
bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two
ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""


def ways(n: int) -> int:
    """
    Return the number of ways to get to the bottom corner
    . . . .  -> 1 1 1  1
    . . . .     1 2 3  4
    . . . .     1 3 6  10
    . . . .     1 4 10 20
    We only need to consider one half really - perhaps
    """
    # Build the grid
    grid = [[1] * n]
    row = 1
    while row < n:
        for i in range(n):
            if i == 0:
                new_row = [1]
            else:
                new_row.append(new_row[i - 1] + grid[row - 1][i])
        grid.append(new_row)
        row += 1

    return grid[-1][-1]


def ways_improved(n: int) -> int:
    """Return the number of ways to the bottom right - improved"""
    oldrow = [1] * n
    row = 1
    while row < n:
        for i in range(n):
            if i == 0:
                newrow = [1]
            else:
                newrow.append(newrow[i-1] + oldrow[i])
        oldrow = newrow
        row += 1

    return newrow[-1]


if __name__ == '__main__':
    assert ways(2) == 2
    assert ways(5) == 70
    print(ways(4))  # 20 Checked on paper

    assert ways_improved(5) == 70
    print(ways_improved(4))  # 20