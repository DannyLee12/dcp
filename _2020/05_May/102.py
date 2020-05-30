"""
Given a list of integers and a number K, return which contiguous elements of
the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return
[2, 3, 4], since 2 + 3 + 4 = 9.
"""


def cont(l: list, K: int) -> list:
    """Return a continuous sublist that adds up to K"""
    n = len(l)
    if sum(l) == K:
        return l
    elif K in l:
        return [K]

    for size in range(n, 2, -1):
        for i in range(n - size + 1):
            if sum(l[i:i + size]) == K:
                return l[i:i + size]


if __name__ == '__main__':
    assert cont([1, 2, 3, 4, 5], 9) == [2, 3, 4]
    assert cont([1, -2, 3, -4, 5], -3) == [-2, 3, -4]
