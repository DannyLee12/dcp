"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string
back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(n: Node, output: dict = {}) -> dict:
    """Create a dict -> json payload"""
    if not any([n.left, n.right]):
        return n.val
    elif not n.left:
        output[n.val] = ["x", serialize(n.right, output)]
    elif not n.right:
        output[n.val] = [serialize(n.left, output), "x"]
    else:
        output[n.val] = [serialize(n.left, output), serialize(n.right, output)]

    return output


def deserialize(s: dict, n: Node = Node('root')) -> Node:
    """Loop through the dict and create a Node from that"""
    if isinstance(s[n.val][0], str):
        # Left
        if s[n.val][0] == 'x':
            pass  # Already set to None
        else:
            n.left = Node(s[n.val][0])
    else:
        # Assume a dict means a node
        n.left = deserialize(s[n.val][0],
                             Node(list(s[n.val][0].keys())[0]))
    if isinstance(s[n.val][1], str):
        # Right
        if s[n.val][1] == 'x':
            pass  # Already set to None
        else:
            n.right = Node(s[n.val][1])
    else:
        # Assume a dict means a node
        n.right = deserialize(s[n.val][1],
                             Node(list(s[n.val][0].keys())[0]))

    return n


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    s = serialize(node)
    nd = deserialize(s)

    assert deserialize(serialize(node)).left.left.val == 'left.left'
