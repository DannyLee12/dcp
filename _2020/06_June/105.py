"""
Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked, f itself will not
be called for N milliseconds.
"""
from typing import Callable
import time
from multiprocessing import Process


def debounced(f: Callable, N: int, val: str, file: str = "/tmp/file") -> None:
    """Call f after N milliseconds"""
    with open(file, "w") as f1:
        f1.write("Ready")
        invoked = "In Progress"
    while invoked == "In Progress":
        time.sleep(1)
        with open(file) as f2:
            invoked = f2.read()
    with open(file, "w") as f3:
        f3.write("In Progress")
    time.sleep(N / 1000)
    f(val)
    with open(file, "w") as f4:
        f4.write("Done")


def fun(val):
    print(val)


if __name__ == '__main__':
    jobs = []
    for i in range(0, 10):
        out_list = list()
        process = Process(target=debounced, args=(fun, 1000, i))
        jobs.append(process)

    # Start the processes (i.e. calculate the random number lists)
    for j in jobs:
        j.start()
