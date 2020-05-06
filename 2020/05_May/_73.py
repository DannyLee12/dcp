"""
Given the head of a singly linked list, reverse it in-place.
"""


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


def reverse(node: LinkedList) -> LinkedList:
    """Reverse a LinkedList in Place"""
    head = True
    while node.next:
        if head:
            prev_node = LinkedList(node.data, None)
            head = False
        else:
            prev_node = current_node

        node = node.next
        current_node = LinkedList(node.data, prev_node)

    return current_node


if __name__ == '__main__':
    l = LinkedList(4, LinkedList(4, LinkedList(6, LinkedList(12))))
    print(l)
    rev_l = reverse(l)
    print(rev_l)
    print(reverse(reverse(l)))

