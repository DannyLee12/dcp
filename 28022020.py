"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and
calls f after n milliseconds.
"""

from time import sleep


def scheduler(func, n):
    sleep(n/1000)
    return func()


def p():
    print("this")


if __name__ == '__main__':
    scheduler(p, 2)
