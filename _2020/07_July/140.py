"""
Given an array of integers in which two elements appear exactly once and all
other elements appear exactly twice, find the two elements that appear only
once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8.
The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""


def get_singletons(l: list) -> (int, int):
    """Return the elements that only exist once"""
    q = set()
    for v in l:
        if v not in q:
            q.add(v)
        else:
            q.remove(v)

    return tuple(q)


if __name__ == '__main__':
    assert get_singletons([2, 4, 6, 8, 10, 2, 6, 10]) == (4, 8)
