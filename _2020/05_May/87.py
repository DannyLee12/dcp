"""
This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A

does not validate, since A cannot be both north and south of C.

A NW B
A N B

is considered valid.
"""

opposites = {"N": "S", "E": "W", "S": "N", "W": "E"}


class Graph:
    s = set()
    N = None
    E = None
    S = None
    W = None

    def __init__(self, rules):
        for rule in rules:
            r = rule.split()
            if not self.s:
                self.N, self.E, self.S, self.W = r[2] * 4
            if r[0] not in self.s:
                for direction in r[1]:
                    setattr(self, direction, r[0])
            if r[2] not in self.s:
                for direction in r[1]:
                    setattr(self, opposites[direction], r[2])
            print(self)

    def __repr__(self):
        return f"N: {self.N}, E: {self.E}, S: {self.S}, W: {self.W}"


def set_rules(s: str) -> Graph:
    """set rules from a string"""
    r = s.split()
    g = Graph(r[2])
    for c in r[1]:
        setattr(g, c, r[0])

    return g


if __name__ == '__main__':
    # g = Graph(["A NE B"])
    # g2 = Graph(["A N B"])
    g3 = Graph(["A N B", "B NE C", "C N A"])
    # r2 = "A SW C"
    # g = set_rules(r1)
    # g2 = set_rules(r2)
    # print(g)
    # print(g2)
    print(g3)