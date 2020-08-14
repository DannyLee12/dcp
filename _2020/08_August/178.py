"""
Alice wants to join her school's Probability Student Club. Membership dues are
computed via one of two simple probabilistic games.


The first game: roll a die repeatedly. Stop rolling once you get a five
followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by
a five.

Which of the two games should Alice elect to play? Does it even matter? Write a
program to simulate the two games and calculate their expected value.
"""
from random import randint


def game1() -> int:
    """Record how many rolls to get a 5 followed by a 6"""
    counter = 0
    roll = 0
    while True:
        prev_roll = roll
        roll = randint(1, 6)
        counter += 1
        if roll == 6 and prev_roll == 5:
            break

    return counter


def game2() -> int:
    """Record how many rolls to get a 6 followed by a 6"""
    counter = 0
    roll = 0
    while True:
        prev_roll = roll
        roll = randint(1, 6)
        counter += 1
        if roll == 5 and prev_roll == 5:
            break

    return counter


if __name__ == '__main__':
    g1 = 0
    for i in range(10000):
        g1 += game1()

    g2 = 0
    for j in range(10000):
        g2 += game2()

    print(g1/i)
    print(g2/j)
    print(g1/g2)
