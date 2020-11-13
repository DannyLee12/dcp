"""
This problem was asked by Indeed.

Given a 32-bit positive integer N, determine whether it is a power of four in
faster than O(log N) time.
"""


def pow_4(i: int) -> bool:
    """Return power of 4 in less than log n"""
    if i & 1 == 1:
        return False
    i = i >> 1
    return not i & 1


def pow_4_log(i: int) -> bool:
    if i % 4 == 0:
        return True


if __name__ == '__main__':
    i = 4
    for i in range(1, 100):
        if pow_4(i):
            print(i)

    print(pow_4(4000000))
