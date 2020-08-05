"""
Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become
-3 -> 1 -> 4 -> 99.
"""

from _2020 import LinkedList


def _sort(l: LinkedList) -> LinkedList:
    """Return a sorted LinkedList"""

    def merge(l1, l2):
        """Merge two Linked Lists"""
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.data < l2.data:
            l = l1
            l.next = merge(l1.next, l2)
        else:
            l = l2
            l.next = merge(l1, l2.next)
        return l

    def merge_sort(h):
        # Base case if head is None
        if h is None or h.next is None:
            return h

        def get_middle(l):
            slow, fast = l, l
            while fast.next.next is not None:
                slow = slow.next
                # Move fast at double the speed of slow
                # Then when fast is done, slow is at the halfway point
                fast = fast.next.next

            return slow

        # Get the value in the middle
        middle = get_middle(h)
        # Get the next value
        next_middle = middle.next
        # Set the next value to None
        middle.next = None
        # Merge sort the head of the LL up to middle
        left = merge_sort(h)
        # Merge sort the rest of the LL
        right = merge_sort(next_middle)

        return merge(left, right)

    return merge_sort(l)


if __name__ == '__main__':
    l = LinkedList(4, LinkedList(1, LinkedList(-3, LinkedList(99))))
    assert _sort(l) == LinkedList(-3, LinkedList(1, LinkedList(4, LinkedList(99))))
