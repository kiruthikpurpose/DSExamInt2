def dfs(graph, start):
    stack = [start]  # Initialize the stack with the starting vertex
    visited = {start}  # Keep track of visited nodes

    while stack:
        temp = stack.pop()
        print(temp, end=" ")


        for neighbor in reversed(graph): 
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

# Input graph as per your format
Graph = {}
n = int(input("Enter no. of vertices: "))  # Number of vertices
for i in range(n):
    a = input()  # Vertex
    b = input().split()  # Neighbors
    Graph[a] = b  # Store vertex and its neighbors

st = input("Enter start element: ")
print()
dfs(Graph, st)  # Call DFS starting from the given start vertex
print()
