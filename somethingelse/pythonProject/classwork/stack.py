class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []
        self.top = -1

    def append(self, value):
        if self.is_full():
            raise Exception('Stack is full. cannot push value.')
        self.stack.append(value)
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty. cannot pop value.')
        self.top -= 1
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty. cannot peek value.')
        return self.stack[self.top]

    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def size(self):
        return self.top + 1

    def search(self, value):
        if self.is_empty():
            raise Exception('Stack is empty. cannot search value.')
        for index in range(self.top + 1):
            if self.stack[index] == value:
                return index
        return -1

