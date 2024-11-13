vertices = int(input())
edges = int(input())

arr = ([0 for i in range(vertices)] for i in range(vertices))

for i in range(edges):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for i in range(vertices):
    for j in range(vertices):
        print(arr[i][j], end = " ")
    print()