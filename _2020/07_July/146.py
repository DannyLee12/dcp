"""
This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that
subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0

should be pruned to:

   0
  / \
 1   0
    /
   1

We do not remove the tree at the root or its left child because it still has a
1 as a descendant.
"""

from _2020 import Tree


def prune(t: Tree) -> Tree:
    """Prune 0s from a binary Tree"""
    if isinstance(t.left, Tree):
        t.left = prune(t.left)
    if isinstance(t.right, Tree):
        t.right = prune(t.right)

    if not t.left and not t.right:
        if t.node == 0:
            del t.node
            return None

    return t


if __name__ == '__main__':
    t = Tree(0, Tree(1), Tree(0, Tree(1, Tree(0), Tree(0)), Tree(0)))
    ts = Tree(0, Tree(1), Tree(0, Tree(1)))
    tp = prune(t)
    assert tp == ts
