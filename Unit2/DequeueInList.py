class DequeList:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        return self.deque.pop(0) if not self.is_empty() else None
    
    def remove_rear(self):
        return self.deque.pop() if not self.is_empty() else None
    
    def peek_front(self):
        return self.deque[0] if not self.is_empty() else None
    
    def peek_rear(self):
        return self.deque[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.deque) == 0
    
    def size(self):
        return len(self.deque)