"""
Given a set of closed intervals, find the smallest set of numbers that covers
all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of
numbers that covers all these intervals is {3, 6}.
"""


def covering(l: list) -> set:
    """Determine the smallest set that covers all intervals"""
    result = set()
    i = 0
    n = len(l)
    l.sort(key=lambda x: x[0])

    while i < n:
        # Iterate through the list of intervals that are NOT in the current
        # set
        interval = l[i]

        # Loop through the remaining intervals until one doesn't overlap
        while i < n:
            if intersecting(l[i], interval):
                # Recalculate the interval such that it just overlaps each
                interval = (max(l[i][0], interval[0]), min(l[i][1], interval[1]))
                i += 1
            else:
                print("Value not intersecting")
                break

        result.add(interval[0])
    return result


def intersecting(x, y):
    """Determine if x and y intersect"""
    return not (x[0] > y[1] or y[0] > x[1])


if __name__ == '__main__':
    print(covering([[0, 3], [2, 6], [3, 4], [6, 9]]))
    print(covering([[0, 3], [1, 12], [2, 6], [3, 4], [6, 12], [13, 17]]))