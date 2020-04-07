"""
Given an array of numbers, find the maximum sum of any contiguous subarray of
the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would
be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would
not take any elements.

Do this in O(N) time.
"""


def max_sum_improved(l: list) -> int:
    """Kadane’s Algorithm, in neat python"""
    max_ending_here, max_so_far = 0, 0

    for x in l:
        max_ending_here += x
        max_ending_here = max(0, max_ending_here)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


if __name__ == '__main__':
    print(max_sum_improved([34, -50, 42, 14, -5, 86, 10, 10, -5, 10, 5, -5, 15]))
    assert max_sum_improved([34, -50, 42, 14, -5, 86]) == 137
    print(max_sum_improved([34, -50, 42, 14, -5, 86, -5, -5, 5, -5, -5, 100]))
