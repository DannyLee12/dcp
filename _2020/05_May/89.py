"""
Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies
the constraint that the key in the left child must be less than or equal to the
root and the key in the right child must be greater than or equal to the root.
"""

from _2020 import Tree


def valid_tree(t: Tree, flag: str = None) -> bool:
    """
    Return whether a binary search tree is valid
    """
    if isinstance(t.left, Tree):
        t.left = valid_tree(t.left, 'l')
    if isinstance(t.right, Tree):
        t.right = valid_tree(t.right, 'r')
    if t.left and t.right:
        if t.left <= t.node <= t.right:
            if t.root:
                return True
            elif flag == 'l':
                # On the left side of the Binary Tree, we are concerned with
                # the larger value (t.right) assuming that tree is valid
                return t.right
            elif flag == 'r':
                return t.left
            else:
                return t.node
    elif t.left:
        if t.left <= t.node:
            if t.root:
                return True
            else:
                return t.node
    elif t.right:
        if t.node <= t.right:
            if t.root:
                return True
            else:
                return t.node

    return t.left <= t.node <= t.right


if __name__ == '__main__':
    # Valid
    t_valid_simple = Tree(2, 1, 3, root=True)
    t_valid_nested = Tree(3, Tree(2, 1), Tree(4, right=5), root=True)
    t_valid_left = Tree(3, Tree(2, 1), 4, root=True)
    t_valid_right = Tree(3, 2, Tree(4, right=5), root=True)
    assert valid_tree(t_valid_simple) is True
    assert valid_tree(t_valid_nested) is True
    assert valid_tree(t_valid_left) is True
    assert valid_tree(t_valid_right) is True
    # Invalid
    t_invalid_simple = Tree(1, 2, 3, True)
    t_invalid_complicated_left = Tree(3, Tree(2, 1, 6), Tree(4, right=5))
    t_invalid_complicated_right = Tree(3, Tree(2, 1), Tree(4, 1, 5))
    t_invalid_complicated = Tree(3, Tree(2, 1, 6), Tree(4, 1, 5))
    assert valid_tree(t_invalid_simple) is False
    assert valid_tree(t_invalid_complicated_left) is False
    assert valid_tree(t_invalid_complicated_right) is False
    assert valid_tree(t_invalid_complicated) is False
