"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its
head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""

from _2020 import LinkedList


def swap(ll: LinkedList) -> LinkedList:
    """Swap every two nodes"""
    counter = 0
    ll_root = LinkedList(None)
    nll = ll_root
    while ll.next:
        if counter % 2 == 0:
            # Swap nodes
            nll.data = ll.next.data
            nll.next = LinkedList(ll.data)
        else:
            nll.next = LinkedList(ll.next.data)
        ll = ll.next
        nll = nll.next
        counter += 1

    return ll_root


if __name__ == '__main__':
    l = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4))))
    l1 = LinkedList(2, LinkedList(1, LinkedList(4, LinkedList(3))))

    s = swap(l)

    assert l1 == s
