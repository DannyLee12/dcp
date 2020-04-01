"""
Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If
    there are no elements in the stack, then it should throw an error or return
    null.
    max(), which returns the maximum value in the stack currently. If there are
    no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
"""


class Stack:
    stack = []
    max_values = []

    def push(self, val):
        """Push a value onto the stack"""
        self.stack.append(val)
        if not self.max_values:
            self.max_values.append(val)
        self.max_values.append(max(val, self.max_values[-1]))

    def pop(self):
        """Pop the value off the top of the stack"""
        val = self.stack.pop()
        if val == self.max_values[-1]:
            self.max_values.pop()

        return val

    def max(self):
        """return max"""
        return self.max_values[-1]


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(3)
    s.push(2)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print("Max", s.max())
    print(s.stack)