"""
Given k sorted singly linked lists, write a function to merge all the lists
into one sorted singly linked list.
"""

from _73 import LinkedList


def merge(*l: LinkedList) -> LinkedList:
    """Merge a few LinkedLists into one"""
    vals = []
    for ll in l:
        vals.append(ll.data)
        current = ll.next
        while current:
            vals.append(current.data)
            current = current.next

    head = True
    for i in reversed(sorted(vals)):
        if head:
            prev_node = None
            head = False
        else:
            prev_node = current_node

        current_node = LinkedList(i, prev_node)

    return current_node


if __name__ == '__main__':
    l1 = LinkedList(1, LinkedList(1))
    l2 = LinkedList(2, LinkedList(2, LinkedList(3)))
    l3 = LinkedList(5)

    lt = merge(l1, l2, l3)
    lr = LinkedList(1,
                    LinkedList(1,
                               LinkedList(2,
                                          LinkedList(2,
                                                     LinkedList(3,
                                                                LinkedList(5)
                                                                )))))

    # print(l1)
    # print(l2)
    # print(l3)
    print(lt)
    print(lr)
