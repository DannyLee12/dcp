"""
Given a mapping of digits to letters (as in a phone number), and a digit
string, return all possible letters the number could represent. You can assume
each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23”
should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""


def mapping(map: dict, num: int) -> list:
    """Return all valid numbers"""
    l = []
    s = str(num)
    n = len(s)
    for x in range(n):
        for y in range(x+1, n):
            l += [i + j for i in map[s[x]] for j in map[s[y]]]

    return l


if __name__ == '__main__':
    print(mapping({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, 23))
    print(mapping({"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g"]}, 234))
    assert mapping({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, 23) == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
