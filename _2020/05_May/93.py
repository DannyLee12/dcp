"""
Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
"""

from _2020 import Tree, valid_tree


def largest_bst(t: Tree) -> Tree:
    """Return the largest bst in a Tree"""

    def size_tree(t, size=0):
        """Calculate the size of a tree"""
        if isinstance(t.left, Tree) and isinstance(t.right, Tree):
            return size_tree(t.left, size + 1) + size_tree(t.right, size + 1)
        else:
            return size + 1

    tv = valid_tree(t)
    if tv:
        return tv


if __name__ == '__main__':
    vt = Tree(2, 1, 3, root=True)
    vt2 = Tree(2, Tree(2, 1), Tree(4, right=5), root=True)

    print(largest_bst(vt))
    print(largest_bst(vt2))
