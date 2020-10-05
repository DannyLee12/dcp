"""
You are given N identical eggs and access to a building with k floors. Your
task is to find the lowest floor that will cause an egg to break, if dropped
from that floor. Once an egg breaks, it cannot be dropped again. If an egg
breaks when dropped from the xth floor, you can assume it will also break when
dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take,
in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every
floor, beginning with the first, until we reach the fifth floor, so our
solution will be 5.
"""


def min_drops(N: int, k: int) -> int:
    """Return the minimum worst case drops"""
    # Worst case is when it breaks on the first floor
    def bin_search(start, end, value, N, drops):
        if N == 1:
            return end + drops
        drops += 1
        midpoint = (start + end) // 2
        if midpoint == value:
            return drops
        return bin_search(start, midpoint, value, N - 1, drops)

    return bin_search(0, k, 1, N, 0)


if __name__ == '__main__':
    print(min_drops(1, 5))
    print(min_drops(20, 10))
    print(min_drops(2, 10))
