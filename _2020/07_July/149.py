"""
Given a list of numbers L, implement a method sum(i, j) which returns the sum
from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]),
which is 5.

You can assume that you can do some pre-processing. sum() should be optimized
over the pre-processing step.
"""
from time import time_ns


class L:
    def __init__(self, l):
        self.cache = {}
        self.l = l

    def sum(self, i, j):
        if i not in self.cache:
            self.cache[i] = {j: sum(self.l[i:j])}
        else:
            if j in self.cache[i]:
                # Direct match
                pass
            else:
                for x in self.cache[i].keys():
                    # Calculate which is quicker, sum or lookup + smaller sum
                    if j - x < j - i:
                        value = self.cache[i][x] + sum(self.l[x:j])
                self.cache[i][j] = value
        return self.cache[i][j]


if __name__ == '__main__':
    l = L([1, 2, 3, 4, 5])
    assert l.sum(1, 3) == 5
    l_large = [x for x in range(1000000)]
    l2 = L(l_large)
    # Create cache
    t = time_ns()
    print(l2.sum(1, 500000))
    t1 = time_ns() - t
    print(f"Time taken for 5000 = {t1}")
    # Get a slightly bigger object
    t = time_ns()
    print(l2.sum(1, 500001))
    t2 = time_ns() - t
    print(f"Time taken for 5001 = {t2}")
    # Confirm the speedup
    assert t2 * 100 < t1
    # Confirm the logic is sound
    assert l.sum(1, 4) == 9
