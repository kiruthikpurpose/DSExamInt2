def dfs(graph, start):
    stack = [start]
    visited = {start}

    while len(stack) > 0:
        temp = stack.pop()
        print(temp, end=" ")

        for res in reversed(graph):
            if res not in visited:
                stack.append(res)
                visited.add(res)

Graph = {}
n = int(input("Enter no. of vertices: "))
for i in range(n):
    a = input() # KEY
    b = input().split() # VALUES
    Graph[a] = b

st = input("Enter start element: ")
print()
dfs(Graph, st)
print()