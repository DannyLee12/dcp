"""
Using a read7() method that returns 7 characters from a file, implement
readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7()
returns “Hello w”, “orld” and then “”.
"""


def read7():
    """Read 7 chars from a file"""
    with open("file.txt") as f:
        global index
        f.seek(index)
        index += 7
        data = f.read(7)

    return data


def readN(n: int) -> str:
    """Read n chars from a file"""
    if n < 7:
        return read7()[:n]
    return read7() + readN(n - 7)


if __name__ == '__main__':
    global index
    index = 0
    r = readN(30)
    print(r)
    assert len(r) == 30
