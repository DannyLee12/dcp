"""
Given a set of closed intervals, find the smallest set of numbers that covers
all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of
numbers that covers all these intervals is {3, 6}.
"""


def smallest_set(l: list) -> set:
    """Return the smallest set that covers all the intervals"""
    s1 = set()
    confirmed_sets = set()
    unconfirmed = []
    for interval in l:
        un_flag = False
        for val in interval:
            if val in s1:
                confirmed_sets.add(val)
                un_flag = True
            else:
                if not un_flag:
                    un_flag = True
                    unconfirmed.append(interval)
            s1.add(val)

    for int in unconfirmed:
        valid = False
        for val in int:
            if val in confirmed_sets:
                valid = True
                break
        if not valid:
            confirmed_sets.add(int[0])

    return confirmed_sets


if __name__ == '__main__':
    print(smallest_set([[0, 3], [2, 6], [3, 4], [6, 9]]))
    print(smallest_set([[0, 3], [1, 12], [2, 6], [3, 4], [6, 12], [13, 17]]))