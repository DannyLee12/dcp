"""
This is your coding interview problem for today.

This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following
should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5

"""

from _2020 import Tree


def node_print(t: Tree, visited=None) -> None:
    """Print nodes in a binary tree row-wise"""
    if not visited:
        visited = [t.node]
    queue = [t]
    while queue:
        n = queue.pop(0)
        if isinstance(n.left, Tree):
            visited.append(n.left.node)
            queue.append(n.left)
        else:
            if n.left:
                visited.append(n.left)
        if isinstance(n.right, Tree):
            visited.append(n.right.node)
            queue.append(n.right)
        else:
            if n.right:
                visited.append(n.right)

    print(visited)


if __name__ == '__main__':
    t1 = Tree(1, 2, Tree(3, 4, 5))
    t2 = Tree(1, Tree(2, right=3), Tree(4, right=5))
    node_print(t1)
    node_print(t2)
