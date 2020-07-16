"""
Given a list of numbers L, implement a method sum(i, j) which returns the sum
from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]),
which is 5.

You can assume that you can do some pre-processing. sum() should be optimized
over the pre-processing step.
"""


class L:
    def __init__(self, l):
        self.cache = {}
        self.l = l

    def sum(self, i, j):
        key = f"{i}{j}"
        if key not in self.cache:
            self.cache[key] = sum(self.l[i: j])
        return self.cache[key]


if __name__ == '__main__':
    l = L([1, 2, 3, 4, 5])
    assert l.sum(1, 3) == 5
