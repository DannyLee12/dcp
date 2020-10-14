"""
One way to unlock an Android phone is through a pattern of swipes across a 1-9
keypad.

For a pattern to be valid, it must satisfy the following:

    All of its keys must be distinct.
    It must not connect two keys by jumping over a third key, unless that key
    has already been used.

For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
"""

g = {1: [2, 4, 5],
     2: [1, 3, 4, 5, 6],
     3: [2, 5, 6],
     4: [1, 2, 5, 8, 7],
     5: [1, 2, 3, 4, 6, 7, 8, 9],
     6: [3, 2, 5, 8, 9],
     7: [4, 5, 8],
     8: [7, 4, 5, 6, 9],
     9: [8, 5, 6]}


def valid_swipes(N: int) -> int:
    """Return the number of valid swipes of length N"""

    def valid_routes(hops, node, total=0):
        """return number of valid hops from a node"""
        if hops == 1:
            return len(g[node])

        for n in g[node]:
            total += valid_routes(hops - 1, n, total)

        return total

    total = 0
    for x in range(1, 2):
        total += valid_routes(N, x)

    return total


if __name__ == '__main__':
    print(valid_swipes(4))
