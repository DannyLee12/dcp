"""
Determine whether a doubly linked list is a palindrome. What if it’s singly
linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""

from _2020 import LinkedList


def palindrome(ll: LinkedList) -> bool:
    """Is the linked list a palindrome"""
    q = []
    node = ll
    while node:
        q.append(node.data)
        node = node.next

    n = len(q)
    if n % 2 == 1:
        if q[:n // 2] == list(reversed(q[n//2 + 1:])):
            return True
    else:
        if q[:n // 2] == list(reversed(q[n // 2:])):
            return True
    return False


if __name__ == '__main__':
    assert palindrome(LinkedList(1, LinkedList(2, LinkedList(2, LinkedList(1)))))
    assert palindrome(LinkedList(1, LinkedList(4, LinkedList(3, LinkedList(4, LinkedList(1))))))
    assert palindrome(LinkedList(1, LinkedList(2, LinkedList(3)))) is False

