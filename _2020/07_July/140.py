"""
Given an iterator with methods next() and hasNext(), create a wrapper iterator,
PeekableInterface, which also implements peek(). peek shows the next element
that would be returned on next().

Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass

"""
from itertools import tee


class PeekableInterface(object):
    def __init__(self, iterator):
        self.i = iterator

    def peek(self):
        self.i, cp = tee(self.i)
        print(next(cp))

    def next(self):
        return next(self.i)

    def hasNext(self):
        self.i, cp = tee(self.i)
        return next(cp) is not None


if __name__ == '__main__':
    i = iter([0, 1, 2, 3])
    pi = PeekableInterface(i)
    pi.peek()  # Prints 0
    assert pi.hasNext()
    assert pi.next() == 0
    assert pi.next() == 1
