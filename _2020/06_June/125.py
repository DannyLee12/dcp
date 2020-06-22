"""
Given the root of a binary search tree, and a target K, return two nodes in
the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15

Return the nodes 5 and 15.
"""

from _2020 import Tree


def get_nodes(t: Tree, K: int) -> tuple:
    """Return two nodes that equal K"""
    if t.left.node + t.right.node == K:
        return t.left.node, t.right.node

    if isinstance(t.left, Tree) and isinstance(t.right, Tree):
        return get_nodes(t.left) or get_nodes(t.right)


if __name__ == '__main__':
    t = Tree(10, Tree(5), Tree(15, 11, 15))
    print(get_nodes(t, 20))
