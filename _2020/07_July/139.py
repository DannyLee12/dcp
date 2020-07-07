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


class PeekableInterface(object):
    def __init__(self, iterator):
        self.i = iterator
        self.prev = []

    def peek(self):
        if self.prev:  # If there is already a value in this queue, return it
            print(self.prev[0])
        else:
            val = next(self.i)
            self.prev.append(val)
            print(val)

    def next(self):
        if self.prev:
            return self.prev.pop()
        return next(self.i)

    def hasNext(self):
        if self.prev:
            return True
        else:
            try:
                val = next(self.i)
                self.prev.append(val)
                return True
            except StopIteration:
                return False


if __name__ == '__main__':
    i = iter([0, 1, 2, 3])
    pi = PeekableInterface(i)
    pi.peek()  # Prints 0
    pi.peek()
    assert pi.hasNext()
    assert pi.next() == 0
    assert pi.next() == 1
    assert pi.next() == 2
    assert pi.next() == 3
    assert pi.hasNext() is False
