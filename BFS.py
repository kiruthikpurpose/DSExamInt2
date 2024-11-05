def bfs(graph, start):
    queue = [start]
    visited = {start}

    while len(queue) > 0:
        temp = queue.pop(0)
        print(temp, end=" ")

        for res in graph:
            if res not in visited:
                queue.append(res)
                visited.add(res)

Graph = {}
n = int(input("Enter no. of vertex: "))
for i in range(n):
    a = input() # key
    b = input().split() # val
    Graph[a] = b

st = input("Enter start element: ")
print()
bfs(Graph, st)
print()