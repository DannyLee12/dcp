"""
This problem was asked by Facebook.

Given a binary tree, return the level of the tree with minimum sum.
"""

from _2020 import Tree


def min_layer(t: Tree) -> int:
    """Determine which layer of a tree has the smallest sum"""
    queue = [t]
    layer = 1
    min_val, min_layer = t.node, layer
    nq = True
    while nq:
        nq = []
        total = 0
        while queue:
            node = queue.pop()
            if isinstance(node, int):
                continue  # Already been counted
            if isinstance(node.left, Tree):
                nq.append(node.left)
                total += node.left.node
            else:
                if node.left:
                    total += node.left
            if isinstance(node.right, Tree):
                nq.append(node.left)
                total += node.right.node
            else:
                if node.right:
                    total += node.right
        layer += 1
        queue = nq
        if total < min_val:
            min_layer, min_val = layer, total

    return min_layer


if __name__ == '__main__':
    t = Tree(1, 2, 3)
    assert min_layer(t) == 1
    t2 = Tree(1,
              Tree(2, 4, Tree(5, -1),
              Tree(3, right=Tree(6, right=1))))
    assert min_layer(t2) == 4
