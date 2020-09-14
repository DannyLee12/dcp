"""
Write a program that computes the length of the longest common subsequence of
three given strings. For example, given "epidemiologist", "refrigeration", and
"supercalifragilisticexpialodocious", it should return 5, since the longest
common subsequence is "eieio".
"""


def longest_subsequence(s1: str, s2: str, s3: str) -> int:
    """Return the longest subsequence of three given strings"""
    # Find the shortest string
    s = min(s1, s2, s3, key=lambda x: len(x))
    total = 0
    ok = False
    while s1:
        for i1, c1 in enumerate(s1):
            for i2, c2 in enumerate(s2):
                if ok:
                    ok = False
                    break
                if c1 == c2:
                    for i3, c3 in enumerate(s3):
                        if c1 == c3:
                            total += 1
                            s1 = s1[i1 + 1:]
                            s2 = s2[i2 + 1:]
                            s3 = s3[i3 + 1:]
                            ok = True
                            break

    return total


if __name__ == '__main__':
    assert longest_subsequence("epidemiologist", "refrigeration",
                        "supercalifragilisticexpialodocious") == 5
