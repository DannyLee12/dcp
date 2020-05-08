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

    def __repr__(self):
        return self._rep(self)

    def _rep(self, tree, val=""):
        val = '\n' + tree.node + '\n'
        if isinstance(tree.left, str):
            val = tree.left + val
        elif isinstance(tree.right, str):
            val = val + tree.right

        if isinstance(tree.left, Tree) and isinstance(tree.right, Tree):
            return self._rep(tree.left) + val + self._rep(tree.right)
        elif isinstance(tree.left, Tree):
            return self._rep(tree.left) + val
        elif isinstance(tree.right, Tree):
            return val + self._rep(tree.right)

        return f"{tree.left} <- {tree.node} -> {tree.right}"


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


if __name__ == '__main__':
    t = Tree("a", Tree("b", "c", "d"), Tree("e", Tree("b", Tree("b", Tree("b", "c", "d"), "d"), "d"), "g"))
    print(t)
    print("\n\n")
    t2 = Tree("a", Tree("b", "c", "d"), "e")
    print(t2)

