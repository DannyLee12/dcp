"""
Design and implement a HitCounter class that keeps track of requests (or hits).
It should support the following operations:

    record(timestamp): records a hit that happened at timestamp
    total(): returns the total number of hits recorded
    range(lower, upper): returns the number of hits that occurred between
    timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
"""


class HitCounter:
    hits = []

    def record(self, timestamp):
        self.hits.append(timestamp)

    def total(self):
        return len(self.hits)

    def range(self, lower, upper):
        l = []
        for x in self.hits:
            if lower <= x <= upper:
                l.append(x)
        return l


if __name__ == '__main__':
    hc = HitCounter()
    hc.record(1)
    hc.record(2)
    hc.record(3)
    hc.record(4)
    hc.record(5)
    assert hc.total() == 5
    assert hc.range(2, 4) == [2, 3, 4]
