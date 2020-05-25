"""
Write a map implementation with a get function that lets you retrieve the value
 of a key at a particular time.

It should contain the following methods:

    set(key, value, time): sets key to value for t = time.
    get(key, time): gets the key at t = time.

The map should work like this. If we set a key at a particular time, it will
maintain that value forever or until it gets set at a later time. In other
words, when we get a key at a time, it should return the value that was set for
that key set at the most recent time.

Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2

d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2

"""
from collections import defaultdict


class Map:
    def __init__(self):
        self.map = defaultdict(dict)

    def set(self, key, value, time):
        try:
            for i in range(self.map[key]["last"][0], time):
                self.map[key][i] = self.map[key]["last"][1]
        except KeyError:
            pass
        self.map[key][time] = value
        self.map[key]["last"] = (time, value)

    def get(self, key, time):
        if time not in self.map[key]:
            if time < self.map[key]["last"][0]:
                return None
            return self.map[key]["last"][1]
        return self.map[key][time]


if __name__ == '__main__':
    d = Map()
    d.set(1, 1, 0)
    d.set(1, 2, 2)
    assert d.get(1, 1) == 1
    assert d.get(1, 3) == 2

    d2 = Map()
    d2.set(1, 1, 5)  # set key 1 to value 1 at time 5
    assert d2.get(1, 0) is None  # get key 1 at time 0 should be null
    assert d2.get(1, 10) == 1  # get key 1 at time 10 should be 1

    d3 = Map()
    d3.set(1, 1, 0)  # set key 1 to value 1 at time 0
    d3.set(1, 2, 0)  # set key 1 to value 2 at time 0
    assert d3.get(1, 0) == 2  # get key 1 at time 0 should be 2
