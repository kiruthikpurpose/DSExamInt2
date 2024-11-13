class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:
            self.front = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item
    
    def peek(self):
        return self.front.data if not self.is_empty() else None
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count