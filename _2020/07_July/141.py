"""
Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass

"""


class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        # If the element exists in the last three items, return it
        if self.list[stack_number - 3] is not None:
            item = self.list[stack_number - 3]
            self.list[stack_number - 3] = None
            # If the last values are None, delete those entries
            if self.list[-3:] == [None] * 3:
                for _ in range(3):
                    self.list.pop()
            return item
        # Else check recursively for the next value
        return self.pop(stack_number - 3)

    def push(self, item, stack_number):
        # If required, extend by three entries
        if not self.list or self.list[stack_number - 3] is not None:
            items = [None, None, None]
            items[stack_number] = item
            self.list.extend(items)
        else:
            self.list[stack_number - 3] = item


if __name__ == '__main__':
    s = Stack()
    s.push(1, 0)
    s.push(4, 2)
    s.push(5, 2)
    s.push(2, 1)
    assert s.pop(0) == 1
    assert s.pop(1) == 2
    assert s.pop(2) == 5
    assert s.pop(2) == 4
    assert s.list == []
