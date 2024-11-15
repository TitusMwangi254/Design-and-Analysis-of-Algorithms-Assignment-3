import heapq

def dijkstra(graph, start):
    """
    Dijkstra's algorithm to find the shortest path from start to all nodes.

    :param graph: Dictionary representing the graph as adjacency lists.
                  {node: [(neighbor, weight), ...]}
    :param start: The starting node.
    :return: Dictionary of shortest distances from start to each node.
    """
    # Priority queue to store (distance, node)
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if the distance is not optimal
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If found a shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage
if __name__ == "__main__":
    # Define the graph
    graph = {
        'A': [('B', 4), ('C', 1)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    
    # Find shortest paths from A
    shortest_paths = dijkstra(graph, 'A')
    print("Shortest paths from A:", shortest_paths)
