"""
Given a start word, an end word, and a dictionary of valid words, find the
shortest transformation sequence from start to end such that only one letter is
changed at each step of the sequence, and each transformed word exists in the
dictionary. If there is no possible transformation, return null. Each word in
the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop",
"dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat",
"dar"}, return null as there is no possible transformation from dog to cat.
"""


def shortest_transformation(start: str, end: str, d: set, path=None) -> list:
    """Return the shortest path from start to end using words in d"""
    if not path:
        path = [start]
    n = len(start)
    if start == end:
        return path

    for word in d:
        for i in range(n):
            if start[:i] + start[i+1:] == word[:i] + word[i+1:]:
                new_word = start[:i] + end[i] + start[1+i:]
                if new_word in d and new_word not in path:
                    path.append(new_word)
                    if shortest_transformation(new_word, end, d, path):
                        return path
                    else:
                        path.pop()


if __name__ == '__main__':
    assert shortest_transformation("dog", "cat", {"dot", "dop", "dat", "cat"}) == ['dog', 'dot', 'dat', 'cat']
    assert shortest_transformation("dog", "cat", {"dot", "tod", "dat", "dar"}) is None
