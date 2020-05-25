"""
Given a number in the form of a list of digits, return all possible
permutations.

For example, given [1,2,3], return
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""


def perms(l: list) -> list:
    """Return all permutations"""
    if len(l) == 1:
        return [l]

    output = []

    for p in perms(l[1:]):
        for i in range(len(l)):
            output.append(p[:i] + [l[0]] + p[i:])

    return output


if __name__ == '__main__':
    print(perms([1, 2, 3]))
    print(perms([1, 2]))
    print(perms([1, 2, 3, 4]))
