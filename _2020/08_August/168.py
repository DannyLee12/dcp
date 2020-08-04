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
from copy import deepcopy


def rotate_90(l: list) -> list:
    """Rotate a N x N matrix by 90 degrees"""
    N = len(l)
    new_list = [[0]* N for _ in range(N)]

    def transpose(l):
        for x in range(N):
            for y in range(N):
                new_list[x][y] = l[y][x]
        return new_list

    def reverse_columns(l):
        new_list = deepcopy(l)
        for i in range(N):
            for j in range(N):
                new_list[i][j] = l[i][N - j - 1]
        return new_list

    return reverse_columns(transpose(l))


if __name__ == '__main__':
    assert rotate_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1],
                                                            [8, 5, 2],
                                                            [9, 6, 3]]
