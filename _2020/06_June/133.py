"""
Given a node in a binary search tree, return the next bigger element, also
known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35

You can assume each node has a parent pointer.
"""

from _2020 import Tree


def get_next(t: Tree, k: int) -> int:
    """Return the smallest element in the right subtree"""
    def smallest_element(t):
        smallest = t.node
        while t.left:
            t = t.left
            smallest = t.node
        return smallest

    while True:
        if k < t.node:
            t = t.left
        elif k > t.node:
            t = t.right
        else:
            if not t.right:
                return t.parent
            else:
                return smallest_element(t.right)


if __name__ == '__main__':
    t = Tree(10, left=Tree(5, parent=10), right=Tree(30, Tree(22, parent=30),
                                                     Tree(35, parent=30), parent=10))

    assert get_next(t, 5) == 10
    assert get_next(t, 10) == 22
    assert get_next(t, 22) == 30
    assert get_next(t, 30) == 35
