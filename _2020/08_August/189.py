"""
Given an array of elements, return the length of the longest subarray where all
its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest
subarray of distinct elements is [5, 2, 3, 4, 1].
"""


def longest_subarray(l: list) -> list:
    """Return the longest subarray containing distinct elements"""
    # For each position in l, get the longest sequence
    s = set()
    longest_list = []
    start = 0
    for i, x in enumerate(l):
        if x in s:
            s = set()
            if i - start > len(longest_list):
                longest_list = l[start: i]
            start = i
        s.add(x)

    if i + 1 - start > len(longest_list):
        longest_list = l[start: i + 1]

    return longest_list


if __name__ == '__main__':
    print(longest_subarray([5, 1, 3, 5, 2, 3, 4, 1]))
