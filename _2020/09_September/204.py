"""
Given a complete binary tree, count the number of nodes in faster than O(n)
time. Recall that a complete binary tree has every level filled except the
last, and the nodes in the last level are filled starting from the left.
"""

from _2020 import Tree


def count_nodes(t: Tree):
    """Count the number of nodes in a complete binary tree"""
    # Get number of levels
    levels = 1
    while t.left:
        levels += 1
        parent = t  # record the parent of the last row
        t = t.left
        t.parent = parent

    nodes = (2 ** (levels - 1)) - 1  # 2^(n-1) - 1 where n is the no of levels

    t = t.parent
    while 1:
        if t.left:
            nodes += 1
        if t.right:
            nodes += 1
            try:
                t = t.parent.right
            except AttributeError:
                break
        else:
            break

    return nodes


if __name__ == '__main__':
    t = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
    assert count_nodes(t) == 7
    t1 = Tree(1, Tree(2, Tree(4)), Tree(3))
    assert count_nodes(t1) == 4
    t2 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3))
    assert count_nodes(t2) == 5
    t3 = Tree(1, Tree(2), Tree(3))
    assert count_nodes(t3) == 3
