class EmptyStackError(Exception):
    pass

class State:
    def __init__(self):
        self.active = False
        self.stacks = ([], [])

    @property
    def stack(self):
        return self.stacks[self.active]

    def toggle(self):
        self.active = not self.active

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            raise EmptyStackError("cannot pop from an empty stack")

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            return None
