"""
Given the root to a binary search tree, find the second largest node in the
tree.
"""


class Tree:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right


if __name__ == '__main__':
    t = Tree(2, Tree(1), Tree(3))
    print(t)
