"""
This problem was asked by Morgan Stanley.

In Ancient Greece, it was common to write text with the first line going
left to right, the second line going right to left, and continuing to go
back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in
boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].
"""

from _2020 import Tree


def bostrophedon(t: Tree) -> list:
    """Return a binary Tree in bostrophedon order"""
    l = [t.node]
    queue = [t]
    ltr = False  # Direction left to right
    while queue:
        e = queue.pop(0)
        if len(queue) == 1:
            ltr = not ltr
        if ltr:
            try:
                l.append(e.left.node)
                l.append(e.right.node)
            except AttributeError:
                break
            queue.append(e.left)
            queue.append(e.right)
        else:
            try:
                l.append(e.right.node)
                l.append(e.left.node)
            except AttributeError:
                break
            queue.append(e.left)
            queue.append(e.right)

    return l


if __name__ == '__main__':
    t = Tree(1,
             Tree(2, Tree(4), Tree(5)),
                  Tree(3, Tree(6), Tree(7)))

    assert bostrophedon(t) == [1, 3, 2, 4, 5, 6, 7]
