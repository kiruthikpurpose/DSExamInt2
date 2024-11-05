class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight):
        self.adjacency_matrix[u][v] = weight
        self.adjacency_matrix[v][u] = weight
    
    def find_min_distance(self, distances, visited):
        min_distance = float('inf')
        min_index = -1
        for vertex in range(self.num_vertices):
            if distances[vertex] < min_distance and not visited[vertex]:
                min_distance = distances[vertex]
                min_index = vertex
        return min_index
    
    def dijkstra(self, source):
        distances = [float('inf')] * self.num_vertices
        distances[source] = 0
        visited = [False] * self.num_vertices
        
        for _ in range(self.num_vertices):
            u = self.find_min_distance(distances, visited)
            visited[u] = True
            for v in range(self.num_vertices):
                if (self.adjacency_matrix[u][v] > 0 and not visited[v] and distances[u] + self.adjacency_matrix[u][v] < distances[v]):
                    distances[v] = distances[u] + self.adjacency_matrix[u][v]
        return distances

num_vertices = int(input("Enter the number of vertices: "))
graph = Graph(num_vertices)

num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    graph.add_edge(u, v, weight)

source_vertex = int(input("Enter the source vertex: "))
shortest_distances = graph.dijkstra(source_vertex)

for distance in shortest_distances:
    print(distance)
