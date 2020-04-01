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
    len_stack = 0
    pos_max = []

    def push(self, val):
        """Push a value onto the stack"""
        self.stack.append(val)
        self.len_stack += 1
        if not self.pos_max:
            self.pos_max.append(0)
        elif val > self.stack[self.pos_max[-1]]:
            self.pos_max.append(self.len_stack - 1)
        else:
            self.pos_max.append(self.pos_max[-1])

    def pop(self):
        """Pop the value off the top of the stack"""
        max_value = self.stack[self.pos_max[-1]]
        val = self.stack.pop()
        if val == max_value:
            self.pos_max[-1] = self.pos_max[-2]
        return val

    def max(self):
        """return max"""
        return self.stack[self.pos_max[-1]]


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(3)
    s.push(2)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.max())
    print(s.stack)