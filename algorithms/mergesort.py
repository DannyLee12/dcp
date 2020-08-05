"""Implementation of Merge Sort for a list"""


def merge_sort(l: list) -> list:
    """Merge sort a list"""
    def merge(l1, l2, l=None):
        if not l:
            l = []
        if not l1:
            return l2
        if not l2:
            return l1
        if l1[0] < l2[0]:
            l.append(l1[0])
            l.extend(merge(l2, l1[1:]))
        else:
            l.append(l2[0])
            l.extend(merge(l2[1:], l1))

        return l

    def _mergesort(l):
        if len(l) <= 1:
            return l

        middle = len(l) // 2
        left = _mergesort(l[:middle])
        right = _mergesort(l[middle:])

        return merge(left, right)

    return _mergesort(l)


if __name__ == '__main__':
    print(merge_sort([5, 4, 3, 2, 1]))
