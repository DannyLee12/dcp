"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses
lst from i to j.
"""


def reverse(lst, i, j):
    """Reverse the list from i to j"""
    def rev(l):
        return l[::-1]

    return lst[:i] + rev(lst[i:j+1]) + lst[j+1:]


if __name__ == '__main__':
    assert reverse([1,2,3,4,5], 1, 3) == [1, 4, 3, 2, 5]
