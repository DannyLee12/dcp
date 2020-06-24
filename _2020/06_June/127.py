"""
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node
represent a digit in the number. The nodes make up the number in reversed
order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5

is the number 54321.

Given two linked lists in this format, return their sum in the same linked list
format.

For example, given

9 -> 9

5 -> 2

return 124 (99 + 25) as:

4 -> 2 -> 1

"""

from _2020 import LinkedList


def sum_ll(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """Sum two linked lists in line"""
    ll3 = LinkedList(None)
    ll = ll3
    count = 0
    while count < 2:
        count = 0
        if not ll.data:
            ll.data = (ll1.data + ll2.data) % 10
            remainder = (ll1.data + ll2.data) // 10
        else:
            ll.next = LinkedList((ll1.data + ll2.data) % 10 + remainder)
            remainder = (ll1.data + ll2.data) // 10
            ll = ll.next

        ll1 = ll1.next
        if ll1 is None:
            count += 1
            ll1 = LinkedList(0)
        ll2 = ll2.next
        if ll2 is None:
            count += 1
            ll2 = LinkedList(0)

    if remainder:
        ll.next = LinkedList(remainder)

    return ll3


if __name__ == '__main__':
    l = LinkedList(4, (LinkedList(2, LinkedList(1))))
    l2 = sum_ll(LinkedList(9, LinkedList(9)), LinkedList(5, LinkedList(2)))
    assert l == l2
    l3 = LinkedList(4, LinkedList(2, LinkedList(1)))
    l4 = sum_ll(LinkedList(4, LinkedList(1, LinkedList(1))), LinkedList(0, LinkedList(1)))
    assert l3 == l4
