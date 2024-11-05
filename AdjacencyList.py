class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class Graph:
    def _init_(self, n):
        self.arr = {i: None for i in range(n)}

    def create(self, a, b): # a = source, b = destination
        newNode = Node(a)
        newNode.next = self.arr[b]
        self.arr[b] = newNode

        newNode = Node(b)
        newNode.next = self.arr[a]
        self.arr[a] = newNode

    def display(self):
        for i in self.arr:
            print(i,':',end=" ")
            temp = self.arr[i]
            while temp:
                print(temp.data, end =",")
                temp = temp.next
            print()

ver = int(input())
edge = int(input())
grf = Graph(ver)
for i in range(edge):
    a,b = map(int,input().split())
    grf.create(a, b)
print()
grf.display()
print()