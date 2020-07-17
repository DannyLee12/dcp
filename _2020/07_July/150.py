"""
Given a list of points, a central point, and an integer k, find the nearest k
points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central
point (1, 2), and k = 2, return [(0, 0), (3, 1)].
"""
from math import sqrt


def closest_points(l: list, cp: tuple, k: int) -> list:
    """Return the k closest points in l to cp"""
    def distance(p1, p2):
        return sqrt(((p1[0] - p2[0]) ** 2) + (p1[1] - p2[1]) ** 2)
    close_points = {}
    largest_distance = float("inf")
    for point in l:
        dis = distance(point, cp)
        if dis < largest_distance:
            if len(close_points) == k:
                # find the largest distance and del it
                del close_points[max(close_points.items(), key=lambda x: x[1])[0]]
                largest_distance = dis
            close_points[point] = dis

    return list(close_points.keys())


if __name__ == '__main__':
    assert closest_points([(0, 0), (5, 4), (3, 1)], (1, 2), 2) == [(0, 0), (3, 1)]
