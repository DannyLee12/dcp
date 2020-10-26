"""
A cryptarithmetic puzzle is a mathematical game where the digits of some
numbers are represented by letters. Each letter represents a unique digit.

For example, a puzzle of the form:

  SEND
+ MORE
--------
 MONEY

may have the solution:

{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}

Given a three-word puzzle like the one above, create an algorithm that finds a
solution.
"""
from random import choice

remainder = 0


def solve_cryparithmetic(l: list) -> dict:
    """Provide a solution to a cryptarithmetic problem with unique digits"""
    n = len(l[0])
    d = {}
    e = []
    letters = set()
    # Start as position -1
    position = 1

    while position < n + 1:
        l1 = l[0][-position]
        l2 = l[1][-position]
        l3 = l[2][-position]
        letters.add(l1)
        letters.add(l2)
        letters.add(l3)

        e.append(f"(d['{l1}'] + d['{l2}'] + rem) % 10 == d['{l3}']")
        e.append(f"(d['{l1}'] + d['{l2}'] + rem) // 10")
        position += 1

    e.append(f"d[l[2][0]] == rem")

    while 1:
        c = choice(range(1, 15))
        for let in letters:
            while c in d.values():
                c = choice(range(0, 9))
            d[let] = c

        b = True
        counter = 0
        rem = 0
        for x in e:
            x = x.replace("rem", str(rem))
            if counter % 2 == 1:
                rem = eval(x)
            else:
                if not eval(x):
                    b = False
                    break
            counter += 1

        if b:
            return d


if __name__ == '__main__':
    d = solve_cryparithmetic(["SEND", "MORE", "MONEY"])
    print(d)
    assert (d["D"] + d["E"]) % 10 == d["Y"]
    assert (d["N"] + d["R"] + (d["D"] + d["E"]) // 10) % 10 == d["E"]
    print(d)
