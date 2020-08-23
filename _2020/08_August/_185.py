"""
Given two rectangles on a 2D graph, return the area of their intersection.
If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}

and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}

return 6.
"""


def area_of_intersection(r1: dict, r2: dict) -> int:
    """Return the area of intersection of two rectangles"""
    left = max(r1["top_left"][0], r2["top_left"][0])
    right = min(r1["top_left"][0] + r1["dimensions"][0],
                r2["top_left"][0] + r2["dimensions"][0])
    top = min(r1["top_left"][1], r2["top_left"][1])
    bottom = max(r1["top_left"][1] - r1["dimensions"][1],
                r2["top_left"][1] - r2["dimensions"][1])

    return (right - left) * (top - bottom)


if __name__ == '__main__':
    r1 = {"top_left": (1, 4), "dimensions": (3, 3)}
    r2 = {"top_left": (0, 5), "dimensions": (4, 3)}
    assert area_of_intersection(r1, r2) == 6
    r4 = {"top_left": (1, 1), "dimensions": (2, 3)}
    r3 = {"top_left": (1, 1), "dimensions": (3, 3)}
    print(area_of_intersection(r3, r4))
