class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueueLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0
    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    def dequeue(self):
        if self.is_empty():
            return None
        head = self.tail.next
        if self.tail == head:
            self.tail = None
        else:
            self.tail.next = head.next
        self.size -= 1
        return head.data
    def peek_front(self):
        return self.tail.next.data if not self.is_empty() else None
    def is_empty(self):
        return self.tail is None
    def current_size(self):
        return self.size