"""
You are given an array of length n + 1 whose elements belong to the set
{1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate.
Find it in linear time and space.
"""


def find_duplicates(l: list) -> int:
    """Return the duplicate in the list"""
    n = len(l) - 1
    return sum(l) - (n * (n + 1) // 2)


if __name__ == '__main__':
    assert find_duplicates([6, 5, 4, 3, 2, 2, 1]) == 2
    assert find_duplicates([x for x in range(1, 100000)] + [99123]) == 99123
