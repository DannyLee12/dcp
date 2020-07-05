"""
Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1

"""

from _2020 import Tree


def min_path_sum(t: Tree) -> int:
    """Recursively get the smallest path"""
    if isinstance(t.left, int) and isinstance(t.right, int):
        return t.node + min(t.left, t.right)
    elif isinstance(t.left, Tree) and isinstance(t.right, Tree):
        return t.node + min(min_path_sum(t.left), min_path_sum(t.right))
    elif isinstance(t.left, Tree) and isinstance(t.right, int):
        return t.node + min(min_path_sum(t.left), t.right)
    elif isinstance(t.left, int) and isinstance(t.right, Tree):
        return t.node + min(min_path_sum(t.right), t.left)
    elif isinstance(t.left, int):
        return t.node + t.left
    elif isinstance(t.right, int):
        return t.node + t.right
    elif isinstance(t.right, Tree):
        return t.node + min_path_sum(t.right)
    elif isinstance(t.left, Tree):
        return t.node + min_path_sum(t.left)


if __name__ == '__main__':
    t = Tree(10, Tree(5, None, 2), Tree(5, None, Tree(1, -1)))
    print(min_path_sum(t))
