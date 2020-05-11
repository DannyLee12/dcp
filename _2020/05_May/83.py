"""
Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f

should become:

  a
 / \
 c  b
 \  / \
  f e  d

"""

from _2020 import Tree


def invert(t: Tree) -> Tree:
    """Invert a binary Tree"""
    if isinstance(t.left, Tree) and isinstance(t.right, Tree):
        t.right, t.left = invert(t.left), invert(t.right)
        return t
    else:
        t.left, t.right = t.right, t.left

    return t


if __name__ == '__main__':
    t1 = invert(Tree("a", "b", "c"))
    t2 = Tree("a", "c", "b")
    assert t1 == t2

    t = Tree("a", Tree("b", "d", "e"), Tree("c", "f"))
    tr = Tree("a", Tree("c", right="f"), Tree("b", "e", "d"))

    assert invert(t) == tr
