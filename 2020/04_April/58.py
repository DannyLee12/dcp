"""
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than
linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return
4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""


def find_index(l: list, k: int) -> int:
    """Return the index of the value in < O(N)"""
    def bin_search(value, list):
        start = 0
        end = len(list) - 1
        while True:
            midpoint = int((start + end) / 2)
            if list[midpoint] == value:
                return midpoint
            elif value < list[midpoint]:
                end = midpoint - 1
            elif value > list[midpoint]:
                start = midpoint + 1
            # Solve if we need to start from the end of the list
            if start >= end:
                if start == 0:
                    end = len(list) - 1
                    start = int((start + end) / 2)

    return bin_search(k, l)


if __name__ == '__main__':
    print(find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2))

    for x in range(13):
        print(x)
        assert find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], x) == x
    assert find_index([13, 18, 25, 2, 8, 10], 8) == 4

    l = [13, 18, 25, 2, 8, 10]
    for i, x in enumerate(l):
        assert find_index(l, x) == i

