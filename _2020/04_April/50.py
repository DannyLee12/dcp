"""
Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   /  \
  +    +
 / \   / \
3  2   4  5

You should return 45, as it is (3 + 2) * (4 + 5).
"""


class Tree:
    def __init__(self, node, left, right, root=False):
        self.node = node
        self.left = left
        self.right = right


def solve(t: Tree) -> int:
    """Solve an arithmetic tree"""
    global value
    global newvalue

    if isinstance(t.left, int):
        exec(f"global value; value = {t.left} {t.node} {t.right}")
        return value

    exec(f"global newvalue; newvalue = solve(t.left) {t.node} solve(t.right)")
    return newvalue


if __name__ == '__main__':
    t = Tree(node="*",
             left=Tree(node="+", left=3, right=2),
             right=Tree(node="+", left=4, right=5),
             root=True)

    t2 = Tree(node="+",
             left=Tree(node="+", left=Tree("-", 5, 5), right=Tree("+", 5, 5)),
             right=Tree(node="+", left=4, right=5),
             root=True)

    print(solve(t))
    print(solve(t2))
