"""Helper script containing useful tools"""


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

    # def __repr__(self):
    #     return self._rep(self)
    #
    # def _rep(self, tree, val=""):
    #     #TODO Fix this
    #     val += f"  {tree.node}\n / \\\n{tree.left}   {tree.right}"
    #     if isinstance(tree.left, str) and isinstance(tree.right, str):
    #         return val
    #     if isinstance(tree.left, Tree):
    #         return val + self._rep(tree.left)
    #     elif isinstance(tree.right, Tree):
    #         return val + self._rep(tree.right)
    #
    #     return self._rep(tree.left) + self._rep(tree.right)


class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self._rep(self)

    def _rep(self, node, val=""):
        if node.next is None:
            return val + str(node.data)
        val += str(node.data) + " -> "
        return self._rep(node.next, val=val)
