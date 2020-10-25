"""
Given an array of integers, find the maximum XOR of any two elements.
"""


def max_xor(l: list) -> int:
    """Return the maximum xor of a list of elements"""
    # Easy enough to do in N^2
    n = len(l)
    max_xor = 0
    for i, x in enumerate(l):
        for j in range(i, n):
            max_xor = max(max_xor, x ^ l[j])

    return max_xor


if __name__ == '__main__':
    print(max_xor([x for x in range(1, 10)]))
    print(max_xor([1, 6, 12, 23, 112]))
    print(max_xor([10, 234, 235, 236, 237]))
