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


def sum_ll_slow(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """Slow simple solution"""
    num1 = str(ll1.data)
    while ll1.next:
        num1 += str(ll1.next)
        ll1 = ll1.next

    num2 = str(ll2.data)
    while ll2.next:
        num2 += str(ll2.next)
        ll2 = ll2.next

    print(num1[::-1])
    print(num2[::-1])

    num3 = str(int(num1[::-1]) + int(num2[::-1]))
    ll3 = LinkedList(num3[-1])
    ll = ll3
    for i, c in enumerate(reversed(str(num3))):
        if i == 0:
            continue
        ll.next = LinkedList(c)
        ll = ll.next

    print(ll3)


if __name__ == '__main__':
    sum_ll_slow(LinkedList(9, LinkedList(9)), LinkedList(5, LinkedList(2)))
