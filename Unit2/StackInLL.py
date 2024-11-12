class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.is_empty():
            return None
        removed_node = self.head
        self.head = self.head.next
        return removed_node.data
    def peek(self):
        return self.head.data if not self.is_empty() else None
    def is_empty(self):
        return self.head is None
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count