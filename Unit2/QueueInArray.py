class QueueArray:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    def enqueue(self, item):
        if self.size < self.capacity:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
            self.size += 1
        else:
            raise OverflowError("Queue is full")
    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    def peek(self):
        return self.queue[self.front] if not self.is_empty() else None
    def is_empty(self):
        return self.size == 0
    def current_size(self):
        return self.size