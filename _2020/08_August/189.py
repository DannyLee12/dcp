"""
Given an array of elements, return the length of the longest subarray where all
its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest
subarray of distinct elements is [5, 2, 3, 4, 1].
"""


def longest_subarray(l: list) -> list:
    """Return the longest subarray containing distinct elements"""
    # For each position in l, get the longest sequence
    n = len(l)
    longest_list = []
    for i in range(n):
        s = set()
        nl = []
        for j in range(i, n):
            if l[j] in s:
                break
            s.add(l[j])
            nl.append(l[j])
        if len(nl) > len(longest_list):
            longest_list = nl

    return longest_list


if __name__ == '__main__':
    print(longest_subarray([5, 1, 3, 5, 2, 3, 4, 1]))
