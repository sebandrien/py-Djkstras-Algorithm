# Importing the heapq module for Priority Queue
import heapq

def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    paths = {vertex: [] for vertex in graph}
    paths[starting_vertex] = [starting_vertex]

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_vertex] + [neighbor]
                heapq.heappush(pq, (distance, neighbor))

    return distances, paths

graph_1 = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 1},
    'D': {'B': 1, 'C': 1},
}

distances, paths = calculate_distances(graph_1, 'A')
print("Shortest distances:", distances)

# Find the farthest node
farthest_node = max(distances, key=distances.get)
print("Farthest node:", farthest_node)

# Get the shortest path to the farthest node
print("Shortest path from starting node to farthest node:", paths[farthest_node])