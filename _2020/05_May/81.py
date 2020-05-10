"""
Given a mapping of digits to letters (as in a phone number), and a digit
string, return all possible letters the number could represent. You can assume
each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23”
should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""


def get_permutations(mapping, digits):

    digit = digits[0]

    if len(digits) == 1:
        return mapping[digit]

    result = []
    for char in mapping[digit]:
        for perm in get_permutations(mapping, digits[1:]):
            result.append(char + perm)
    return result


if __name__ == '__main__':
    print(get_permutations({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, "23"))
    print(get_permutations({"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g"]}, "234"))
    assert get_permutations({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, "23") == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
