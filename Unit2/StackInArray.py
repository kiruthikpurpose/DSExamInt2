class StackArray:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def push(self, item):
        if self.top < self.capacity - 1:
            self.top += 1
            self.stack[self.top] = item
        else:
            raise OverflowError("Stack is full")
        
    def pop(self):
        if self.is_empty():
            return None
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item
    
    def peek(self):
        return self.stack[self.top] if not self.is_empty() else None
    
    def is_empty(self):
        return self.top == -1
    
    def size(self):
        return self.top + 1