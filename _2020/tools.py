"""Helper script containing useful tools"""


class Tree:
    def __init__(self, node, left=None, right=None, root=False, parent=None):
        self.node = node
        self.left = left
        self.right = right
        self.root = root
        self.parent = parent

    def __eq__(self, other):
        try:
            if all([self.node == other.node,
                    self.left == other.left,
                    self.right == other.right,
                    self.root == other.root]):
                return True
        except AttributeError:
            return False
        return False

    def __repr__(self):
        return self._rep(self)

    def _rep(self, tree, val=""):
        val = '\n' + str(tree.node) + '\n'
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


def valid_tree(t: Tree, flag: str=None, calls=0) -> (bool, int):
    """
    Return whether a binary search tree is valid
    """
    calls += 1
    if isinstance(t.left, Tree):
        t.left = valid_tree(t.left, 'l', calls)
    if isinstance(t.right, Tree):
        t.right = valid_tree(t.right, 'r', calls)
    if t.left and t.right:
        if t.left <= t.node <= t.right:
            if t.root:
                return True, calls
            elif flag == 'l':
                # On the left side of the Binary Tree, we are concerned with
                # the larger value (t.right) assuming that tree is valid
                return t.right
            elif flag == 'r':
                return t.left
            else:
                return t.node
    elif t.left:
        if t.left <= t.node:
            if t.root:
                return True, calls
            else:
                return t.node
    elif t.right:
        if t.node <= t.right:
            if t.root:
                return True, calls
            else:
                return t.node

    return t.left <= t.node <= t.right, calls


class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.total = 0

    def __repr__(self):
        return self._rep(self)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if isinstance(self, LinkedList) and isinstance(other, LinkedList):
            return self.data == other.data and self.next == other.next
        return self == other

    def _rep(self, node, val=""):
        if node.next is None:
            return val + str(node.data)
        val += str(node.data) + " -> "
        return self._rep(node.next, val=val)

    def __len__(self):
        if self.total:
            return self.total
        c = self
        while isinstance(c.next, LinkedList):
            self.total += 1
            c.next = c.next.next
        self.total += 1
        return self.total
