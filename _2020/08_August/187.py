"""
You are given given a list of rectangles represented by min and max x- and
y-coordinates. Compute whether or not a pair of rectangles overlap each other.
If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}

return true as the first and third rectangle overlap each other.
"""
from _185 import area_of_intersection


def overlapping(l: list) -> bool:
    """Determine if any of the rectangles overlap"""
    for i, r1 in enumerate(l):
        for j, r2 in enumerate(l):
            if i == j:
                continue
            if area_of_intersection(r1, r2):
                return True
    return False


if __name__ == '__main__':
  l = [{"top_left":(1,4),"dimensions":(3,3)},
       {"top_left":(-1,3),"dimensions":(2,1)},
       {"top_left":(0,5),"dimensions":(4,3)}]

  assert overlapping(l)
