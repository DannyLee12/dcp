"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand. Find the minimum element in O(log N) time. You may assume the
array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.

"""


def find_min(l: list) -> int:
    """Find the minimum value in logN"""
    # Some sort of binary search
    def bin_search(l, start, stop):
        midpoint = start + ((stop - start) // 2)
        if l[midpoint] > l[midpoint + 1]:
            return l[midpoint + 1]
        elif l[start] < l[midpoint]:
            return bin_search(l, midpoint, stop)
        else:
            return bin_search(l, start, midpoint)

    return bin_search(l, 0, len(l) - 1)


if __name__ == '__main__':
    print(find_min([5, 7, 10, 3, 4]))
    print(find_min([5, 7, 11, 12, 3, 4]))
    print(find_min([12, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
