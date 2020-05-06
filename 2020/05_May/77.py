"""
Given a list of possibly overlapping intervals, return a new list of intervals
where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return
[(1, 3), (4, 10), (20, 25)].
"""


def new_intervals(l: list) -> list:
    """return a new interval without overlapping intervals"""
    for i, s in enumerate(l):
        for t in l:
            if s == t:
                continue
            if s[0] > t[0] and s[1] < t[1]:
                l.pop(i)

    return l


def new_ints(l: list) -> list:
    """return a new interval without overlapping intervals"""
    result = []
    for i, (j, k) in enumerate(sorted(l, key=lambda x: x[0])):
        if not result:
            result.append((j, k))
        else:
            if prev[0] < j and prev[1] < k:
                result.append((j, k))
        prev = j, k

    return result


if __name__ == '__main__':
    print(new_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]))
    print(new_ints([(1, 3), (5, 8), (4, 10), (20, 25)]))