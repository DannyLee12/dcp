"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses
lst from i to j.
"""


def reverse(lst, i, j):
    """Reverse the list from i to j"""
    def rev(l):
        return l[::-1]

    return lst[:i] + rev(lst[i:j+1]) + lst[j+1:]


def pancake_sort(l: list) -> list:
    """Sort a list using reverse"""
    i = 0
    j = len(l)
    while i < j:
        for idx, x in enumerate(l):
            if idx <= i:
                continue
            if x < l[i]:
                l = reverse(l, i, idx)
        i += 1
    return reverse(l, i, j)


if __name__ == '__main__':
    assert pancake_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert pancake_sort([1, 3, 2, 4, 5]) == [1, 2, 3, 4, 5]
    assert pancake_sort([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]

