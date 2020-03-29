"""
Given an array of integers where every integer occurs three times except for
one integer, which only occurs once, find and return the non-duplicated
integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13],
return 19.

Do this in O(N) time and O(1) space.
"""


def duplicates(l: list) -> int:
    """
    Determine which element is not duplicated 3 times
    :param l: list to check
    :return:
    """
    queue = set()
    queue2 = set()
    for x in l:
        if x in queue:
            if x in queue2:
                queue.discard(x)
            else:
                queue2.add(x)
        else:
            queue.add(x)

    return (queue - queue2).pop()


if __name__ == '__main__':
    print(duplicates([6, 1, 3, 3, 3, 6, 6]))
    print(duplicates([13, 19, 13, 13]))
