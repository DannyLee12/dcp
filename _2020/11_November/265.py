"""
MegaCorp wants to give bonuses to its employees based on how many lines of
codes they have written. They would like to give the smallest positive amount
to each worker consistent with the constraint that if a developer has written
more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine
how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4,
2, 1].
"""


def bonuses(l: list) -> list:
    """Return the minimum amount of bonuses that can be returned"""
    n = len(l)
    bonus_list = [1] * n

    for i, loc in enumerate(l):
        if i == 0:
            continue
        if loc > l[i - 1]:
            bonus_list[i] = bonus_list[i-1] + 1

    for j, loc in enumerate(reversed(l)):
        if j == 0:
            continue
        if loc > l[n - j]:
            bonus_list[n - j - 1] = max(bonus_list[n - j] + 1,
                                        bonus_list[n - j - 1])

    return bonus_list


if __name__ == '__main__':
    assert bonuses([10, 40, 200, 1000, 60, 30]) == [1, 2, 3, 4, 2, 1]
    print(bonuses([10, 40, 200, 1000, 60, 30, 40, 100, 1000, 20, 10]))
