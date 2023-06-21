'''

Data Structure: Graph
Algorithm: Breadth-First Search (BFS)

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Space Complexity: O(V), where V is the number of vertices in the graph.
Time 50 mins
'''
from collections import defaultdict, deque


def shortest_alternating_path(origin, destination, edges):
    # Construct the graph
    graph = defaultdict(list)
    for src, dest, color in edges:
        graph[src].append((dest, color))

    # Perform BFS
    queue = deque([(origin, 0, None)])  # (node, length, prev_color)
    visited = set([(origin, None)])
    while queue:
        node, length, prev_color = queue.popleft()
        if node == destination:
            return length

        for neighbor, color in graph[node]:
            if (neighbor, color) not in visited and color != prev_color:
                queue.append((neighbor, length + 1, color))
                visited.add((neighbor, color))

    return -1


# Test cases
input_edges = [('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), ('B', 'E', "blue"), ('C', 'B', "red"),
               ('D', 'C', "blue"), ('A', 'D', "red"),
               ('D', 'E', "red"), ('E', 'C', "red")]
input_origin = 'A'
input_destination = 'E'
print(shortest_alternating_path(input_origin, input_destination, input_edges))  # Output: 4

input_origin = 'E'
input_destination = 'D'
print(shortest_alternating_path(input_origin, input_destination, input_edges))  # Output: -1
