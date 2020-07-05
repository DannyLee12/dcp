"""
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each
index.

    init(size): initialize the array with size
    set(i, val): updates index at i with val where val is either 1 or 0.
    get(i): gets the value at index i.

"""


class BitArray:
    def __init__(self, size):
        self.ba = 0
        self.size = size

    def set(self, i, val):
        if not 0 <= i <= self.size:
            raise ValueError("Value not in range")
        if val:  # Set to 1
            self.ba |= i
        else:  # Set to 0
            self.ba &= ~i

    def get(self, i):
        if self.ba & i:
            return 1
        return 0


if __name__ == '__main__':
    ba = BitArray(100)
    ba.set(4, 1)
    assert ba.get(4) == 1
    ba.set(4, 0)
    ba.set(5, 1)
    assert ba.get(4) == 0
    assert ba.get(5) == 1
