"""
Given a sorted list of integers, square the elements and give the output in
sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""


def sorted_squares(l: list) -> list:
    """Return a sorted list of squares given a sorted list"""
    nl = []
    n = len(l)
    front_ptr, end_ptr = 0, n - 1
    while front_ptr <= end_ptr:
        front = l[front_ptr] ** 2
        end = l[end_ptr] ** 2
        if front > end:
            nl.insert(0, front)
            front_ptr += 1
        else:
            nl.insert(0, end)
            end_ptr -= 1

    return nl


if __name__ == '__main__':
    assert sorted_squares([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
