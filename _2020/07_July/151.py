"""
Given a 2-D matrix representing an image, a location of a pixel in the screen
and a color C, replace the color of the given pixel and all adjacent same
colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G'
for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B

"""


def replace_color(l: list, pixel: tuple, new_color: str) -> list:
    """Replace all adjacent pixels with the new color"""
    m = len(l)  # row
    n = len(l[0])  # column

    def dfs(p, color, old_color, l, visited=None):
        if not visited:
            visited = []
        if p not in visited:
            if l[p[1]][p[0]] == old_color:
                l[p[1]][p[0]] = color
            visited.append(p)
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= p[1] + x < n and 0 <= p[0] < m:
                    dfs((p[1] + x, p[0] + y), color, old_color, l, visited)
        return l

    return dfs(pixel, "G", l[pixel[0]][pixel[1]], l)


if __name__ == '__main__':
    board = """B B W
W W W
W W W
B B B"""
    l = [x.split(" ") for x in board.split("\n")]
    solved_list = replace_color(l, (2, 2), "G")
    board_solved = """B B G
G G G
G G G
B B B"""

    assert [y.split(" ") for y in board_solved.split("\n")]  == solved_list
