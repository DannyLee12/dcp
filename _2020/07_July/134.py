"""
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the
same interface:

    init(arr, size): initialize with the original large array and size.
    set(i, val): updates index at i with val.
    get(i): gets the value at index i.

"""
from random import random


class SparseArray:
    d = {}

    def init(self, arr: list, size: int):
        for i, x in enumerate(arr):
            if x:  # Ignore 0s
                self.d[i] = x

    def set(self, i, val):
        self.d[i] = val

    def get(self, i):
        try:
            return self.d[i]
        except KeyError:
            return 0


if __name__ == '__main__':
    sa = SparseArray()
    large_list = []
    for x in range(1000):
        if random() < 0.1:
            large_list.append(int(random() * 100))
        large_list.append(0)

    sa.init(large_list, len(large_list))

    sa.set(20, -1)
    sa.set(12000, -1)
    assert sa.get(20) == -1
    assert sa.get(12000) == -1
    assert sa.get(1000000) == 0
