"""
Given pre-order and in-order traversals of a binary tree, write a function to
reconstruct the tree.

For example, given the following preorder traversal:
[a, b, d, e, c, f, g]
And the following inorder traversal:
[d, b, e, a, f, c, g]
You should return the following tree:
    a
   / \
  b   c
 / \ / \
d  e f  g
"""


class Tree:
    def __init__(self, node, left=None, right=None, root=False):
        self.node = node
        self.left = left
        self.right = right
        self.root = root

    def __eq__(self, other):
        if all([self.node == other.node,
                self.left == other.left,
                self.right == other.right,
                self.root == other.root]):
            return True
        return False


def create_tree(inorder: list, preorder: list) -> Tree:
    """Create a Tree from a preorder and inorder traversal"""
    # Set root node
    n = len(inorder)
    root = preorder[0]
    t = Tree(preorder.pop(0), root=True)

    pos = "left"
    while preorder:
        if preorder[0] == root:
            preorder.pop(0)
            continue
        if inorder[0] == root:
            pos = "right"
            inorder.pop(0)
        if sorted(preorder[0:3]) == sorted(inorder[0:3]):
            t.__setattr__(pos, Tree(preorder[0], Tree(preorder[1]), Tree(preorder[2])))
            del preorder[0:3]
            del inorder[0:3]

    return t


if __name__ == '__main__':
    t = Tree(node="a",
             left=Tree("b", Tree("d"), Tree("e")),
             right=Tree("c", Tree("f"),Tree("g")),
             root=True)
    r = create_tree(['d', 'b', 'e', 'a', 'f', 'c', 'g'],
                ['a', 'b', 'd', 'e', 'c', 'f', 'g'])

    assert t == r
