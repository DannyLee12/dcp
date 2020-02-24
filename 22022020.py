"""
Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.
You can modify the input array in-place.
"""


def brute_force(l: list) -> int:
    """Probably not worth doing but n^2 log(n) Worst case"""
    l.sort()
    counter = l[0]
    for i, val in enumerate(l):
        if val < 0:
            continue
        try:
            if l[i + 1] != l[i] + 1:
                return l[i] + 1
        except IndexError:
            return val + 1


def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1


def faster_soln(nums):
    """Check if that value exists in the array"""
    n = max(nums)
    for i in range(1, n):
        if i not in nums:
            return i
    return n + 1


if __name__ == '__main__':
    assert brute_force([3, 4, -1, 1]) == 2
    assert brute_force([1, 2, 0]) == 3
    assert brute_force([3, 4, 1, 2, 6, 8, 9]) == 5
    assert first_missing_positive([3, 4, 1, 2, 6, 8, 9]) == 5
    assert faster_soln([3, 4, 1, 2, 6, 8, 9]) == 5
