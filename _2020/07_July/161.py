"""
This is your coding interview problem for today.

This problem was asked by Square.

Given a list of words, return the shortest unique prefix of each word. For
example, given the list:

    dog
    cat
    apple
    apricot
    fish

Return the list:

    d
    c
    app
    apr
    f

"""


def shortest_prefix(l: list) -> list:
    """Return the shortest prefix of a list of words"""
    n = len(l)
    i = 0
    while i < n:
        x, max_x = 0, 0
        for j in range(n):
            if i == j:
                continue
            while l[i][x] == l[j][x]:
                x += 1
                max_x = max(max_x, x)
        l[i] = l[i][:max_x + 1]
        i += 1

    return l


if __name__ == '__main__':
    assert shortest_prefix(["dog", "cat", "apple", "apricot", "fish"]) == \
           ["d", "c", "app", "apr", "f"]
