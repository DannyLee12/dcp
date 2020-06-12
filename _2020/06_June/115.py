"""
Given two non-empty binary trees s and t, check whether tree t has exactly the
same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The trees could
also be considered as a subtree of itself.
"""

from _2020 import Tree


def t_in_s(t: Tree, s: Tree) -> bool:
    """Return if t is in s"""
    if t == s:
        return True

    if isinstance(s.left, Tree) and isinstance(s.right, Tree):
        return t_in_s(t, s.left) or t_in_s(t, s.right)
    elif isinstance(s.right, Tree):
        return t_in_s(t, s.right)
    elif isinstance(s.left, Tree):
        return t_in_s(t, s.left)

    return False


if __name__ == '__main__':
    t1 = Tree(1, 2, 3)
    s1 = Tree(5, Tree(1, 2, 3))
    assert t_in_s(t1, s1)
    t2 = Tree(1, 2, 3)
    s2 = Tree(5, Tree(1, 2, 4))
    assert t_in_s(t2, s2) is False
    assert t_in_s(t1, t1)
    s3 = Tree(5, Tree(3, Tree(2, Tree(2, Tree(1), Tree(1, 2, 3)))))
    assert t_in_s(t1, s3)

