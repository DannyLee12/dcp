"""
Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""

from random import random, randint


class Tree:
    def __init__(self, node):
        self.node = node

    @property
    def left(self):
        if random() > 0.09:
            return Tree(randint(0, 10))
        return randint(0, 10)

    @property
    def right(self):
        if random() > 0.09:
            return Tree(randint(0, 10))
        return randint(0, 10)


if __name__ == '__main__':
    t = Tree(1)
    while True:
        t = t.left
        print(t)
        if isinstance(t, int):
            break
