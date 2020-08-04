"""
Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Follow-up: What if you couldn't use any extra space?
"""


def rotate_90(l: list) -> list:
    """Rotate a N x N matrix by 90 degrees"""
    N = len(l)

    def transpose(l):
        for x in range(N):
            for y in range(x, N):
                t = l[x][y]
                l[x][y] = l[y][x]
                l[y][x] = t
        return l

    def reverse_columns(l):
        for i in range(N):
            for j in range(N//2):
                t = l[i][j]
                l[i][j] = l[i][N - j - 1]
                l[i][N - j - 1] = t
        return l

    return reverse_columns(transpose(l))


if __name__ == '__main__':
    assert rotate_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1],
                                                            [8, 5, 2],
                                                            [9, 6, 3]]

    assert rotate_90([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]]) == [[13, 9, 5, 1],
                                            [14, 10, 6, 2],
                                            [15, 11, 7, 3],
                                            [16, 12, 8, 4]]
