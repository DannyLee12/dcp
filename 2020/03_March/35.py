"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the
values of the array so that all the Rs come first, the Gs come second,
and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should
become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""


def order_array(l: list):
    n = len(l)
    # Declare pointers
    R = 0
    G, B = n - 1, n - 1

    while R < G and R < B:
        if l[R] == 'R':
            R += 1
        elif l[R] == 'G':
            l[R], l[G] = l[G], l[R]
            G -= 1
        elif l[R] == 'B':
            l[R], l[B] = l[B], l[R]
            B -= 1

    return l


if __name__ == '__main__':
    print(order_array(["R", "G", "B"]))
    print(order_array(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
