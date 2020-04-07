"""
Given an array of numbers, find the maximum sum of any contiguous subarray of
the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would
be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would
not take any elements.

Do this in O(N) time.
"""


def max_sum(l: list) -> int:
    """Return the largest sum of an continuous array"""
    largest = 0
    old_largest = 0
    skip = -1
    for i, x in enumerate(l):
        if skip == i:
            continue
        elif x > 0:
            largest += x
        elif sum(l[i:i+2]) > 0:
            largest += sum(l[i:i+2])
            # Skip the value in 2 iterations as it's already counted
            skip = i + 1
        else:
            old_largest = max(largest, old_largest)
            largest = 0

    return max(largest, old_largest)


if __name__ == '__main__':
    print(max_sum([34, -50, 42, 14, -5, 86, 10, 10, -5, 10, 5, -5, 15]))
    print(max_sum([34, -50, 42, 14, -5, 86]))
    print(max_sum([34, -50, 42, 14, -5, 86, -5, -5, 20]))
