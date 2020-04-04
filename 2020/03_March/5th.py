"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be
    smaller than or equal to N.

You should be as efficient with time and space as possible.
"""


class Log:
    log = []

    def record(self, order_id: str) -> None:
        """Add items to the queue"""
        self.log.append(order_id)

    def get_last(self, i: int) -> str:
        """Get the ith element from the end of the queue"""
        return self.log[-i]


if __name__ == '__main__':
    l = Log()
    l.record("1")
    l.record("2aasdf")
    l.record("3aasdadsfsdf")

    for i in range(1, 4):
        print(l.get_last(i))
