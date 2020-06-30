"""
Given the head to a singly linked list, where each node also has a “random”
pointer that points to anywhere in the linked list, deep clone the list.
"""

from _2020 import LinkedList


class LinkedListRandom(LinkedList):

    def __init__(self, data, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random


def clone(head: LinkedListRandom) -> LinkedListRandom:
    """Deep copy a linkedlist"""
    ll = LinkedListRandom(head.data)
    lp = ll
    while head.next:
        lp.next = LinkedListRandom(head.next.data)
        lp.random = head.random
        head = head.next
        lp = lp.next

    return ll


if __name__ == '__main__':
    l2 = LinkedListRandom(2)
    l1 = LinkedListRandom(1, l2, l2)
    l = LinkedListRandom(0, l1, l2)

    print(clone(l))
