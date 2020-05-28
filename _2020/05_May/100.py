"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the
points. Give the minimum number of steps in which you can achieve it. You start
from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move
from (1, 1) to (1, 2).
"""


def count_steps(l: list) -> int:
    """Return the minimum number of steps to get through the list of points"""
    def in_range(point1, point2):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if point1[0] + i == point2[0] and point1[1] + j == point2[1]:
                    return True
        return False

    def minimize_distance(point1, point2):
        min_distance = float("inf")
        point = (0, 0)
        for i in range(-1, 2):
            for j in range(-1, 2):
                distance = abs(point1[0] + i - point2[0]) + abs(point1[1] + j - point2[1])
                if distance < min_distance:
                    min_distance = distance
                    point = (point1[0] + i, point1[1] + j)
        return point

    total = 0
    while len(l) > 1:
        if in_range(l[0], l[1]):
            l.pop(0)
            total += 1
        else:
            # Add a point to minimize the distance
            l.insert(1, minimize_distance(l[0], l[1]))

    return total


if __name__ == '__main__':
    assert count_steps([(0, 0), (1, 1), (1, 2)]) == 2
    assert count_steps([(0, 0), (3, 3)]) == 3
    assert count_steps([(3, 1), (0, 0)]) == 3
    assert count_steps([(100, 200), (12, 30)]) == count_steps([(12, 30), (100, 200)])
