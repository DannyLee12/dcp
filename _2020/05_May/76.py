"""
You are given an N by M 2D matrix of lowercase letters. Determine the minimum
number of columns that can be removed to ensure that each row is ordered from
top to bottom lexicographically. That is, the letter at each column is
lexicographically later as you go down each row. It does not matter whether
each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi

This is not ordered because of the a in the center. We can remove the second
column to make it ordered:

ca
df
gi

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef

Your function should return 0, since the rows are already ordered (there's only
one row).

As another example, given the following table:

zyx
wvu
tsr

Your function should return 3, since we would need to remove all the columns to
order it.
"""


def remove_columns(l: list) -> int:
    """Determine how many columns are out of order"""
    total = 0
    n = len(l[0])
    m = len(l)
    for i in range(n):
        for j in range(m - 1):
            if l[j][i] > l[j+1][i]:
                total += 1
                break

    return total


if __name__ == '__main__':
    l = """cba
daf
ghi""".split("\n")
    l2 = """zyx
wvu
tsr""".split("\n")

    print(remove_columns(l))
    print(remove_columns(l2))
    print(remove_columns("abcdef".split("\n")))
