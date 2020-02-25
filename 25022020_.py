"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa',
'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def decode(message: str) -> int:
    """Get the number of ways a message can be decoded"""
    messages = []
    total = 0
    n = len(message)
    r = [str(x) for x in range(26)]
    for slice_size in range(2, n + 1):
        decodable = True
        for i, _ in enumerate(message):
            if i + slice_size > n:
                continue
            s = message[i:i + slice_size]
            s2, s3 = None, None
            if n % slice_size != 0:
                s2 = message[i + slice_size:]
                s3 = message[:i]
                if s2 and s2 not in r:
                    decodable = False
                elif s3 and s3 not in r:
                    decodable = False
            if s not in r:
                decodable = False
        if decodable:
            total += 2
    return total + 1


if __name__ == '__main__':
    print(decode('27'))
