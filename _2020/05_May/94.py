"""
Given a binary tree of integers, find the maximum path sum between two nodes.
The path must go through at least one node, and does not need to go through the
root.
"""

from _2020 import Tree


def max_path(t: Tree, max_so_far=float("-inf")):
    """Return the maximum path through a tree including a node"""
    # 1. Start at the root
    # 2. If the root + node.left > root - increase down that path
    # 3. If root + node.left <= 0 - Start again
    # 4. Do the same for the right node - recursively
    # 5. Return the max of left and right

    if isinstance(t.left, Tree) and isinstance(t.right, Tree):
        max_so_far = max(max_path(t.left, max_so_far), max_path(t.right, max_so_far))
        max_so_far = max(max_so_far, max_so_far + t.node)
    else:
        max_ending_here = max(t.node + t.left, t.node + t.right, 0)
        max_so_far = max(max_ending_here, max_so_far)

    return max(max_so_far, t.node)


if __name__ == '__main__':
    t = Tree(1, 2, 1)
    # Simple case
    assert max_path(t) == 3
    t2 = Tree(1, Tree(1, 1, 1), Tree(2, 2, 2))
    assert max_path(t2) == 5
    t3 = Tree(1, Tree(-1, -2, -3), Tree(-1, -2, -3))
    assert max_path(t3) == 1
    t4 = Tree(-1, Tree(2, 1, 1), Tree(0, 1, 2))
    assert max_path(t4) == 3
    t5 = Tree(0, left=Tree(-1, Tree(2, 2, 3), Tree(-1, -2, -3)),
                 right=Tree(-1, Tree(1, 2, 1), Tree(-1, -2, -3)))
    assert max_path(t5) == 5
