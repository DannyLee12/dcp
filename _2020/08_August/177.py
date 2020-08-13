"""
Given a linked list and a positive integer k, rotate the list to the right by
k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become
3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become
3 -> 4 -> 5 -> 1 -> 2.
"""

from _2020 import LinkedList


def rotate_linked_list(ll: LinkedList, k: int) -> LinkedList:
    """Rotate a linked list to the right by k spaces"""
    n = len(ll)
    if k > n:
        k = k % n

    if not k:
        return ll

    current = ll.head

    for _ in range(n - k - 1):
        current = current.next

    kth_node = current

    while current.next:
        current = current.next

    current.next = ll.head
    ll.head = kth_node.next
    kth_node.next = None

    return ll


if __name__ == '__main__':
    ll = LinkedList()
    for x in range(6, 0, -1):
        ll.push(x)

    for y in range(10):
        print(rotate_linked_list(ll, 1))
