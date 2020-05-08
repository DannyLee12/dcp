"""
Given the root of a binary tree, return a deepest node. For example,
in the following tree, return d.

    a
   / \
  b   c
 /
d

"""

from _2020 import Tree


def deepest_node(t: Tree) -> str:
    """Return the deepest Node in a binary tree"""
    g = {}

    def depth(t: Tree, g:dict, current_depth: int=0):
        for n in [t.left, t.right]:
            if isinstance(n, Tree):
                g = depth(n, g, current_depth + 1)
            else:
                if n:
                    g[n] = current_depth + 1

        return g

    return max(depth(t, g).items(), key=lambda x: x[1])[0]


if __name__ == '__main__':
    t = Tree("a", Tree("b", "d"), "c")
    print(deepest_node(t))
    t = Tree("a", Tree("b", "d"), Tree("c", "e"))
    print(deepest_node(t))
    t2 = Tree("a", "b", "c")
    print(deepest_node(t2))
    t3 = Tree("a", Tree("b", "c"), Tree("d", Tree("e", "f")))
    print(deepest_node(t3))
