"""
Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""

from random import random, randint

from _2020 import Tree


def generate() -> Tree:
    """Generate a generator of a Tree of arbitary size"""
    t = Tree(randint(0, 10))
    ran = random()
    while ran < 0.9:
        t.right = Tree(randint(0, 10))
        t.left = Tree(randint(0, 10))
        yield t
        if random() > 0.5:
            t = t.left
        else:
            t = t.right
        ran = random()


if __name__ == '__main__':
    for i in generate():
        print(i.left)
