from collections import defaultdict
import collections

def create_graph(edges):
    graph = defaultdict(list)
    nodes = set()

    for x, y in edges:
        graph[x].append(y)
        nodes.add(x)
        nodes.add(y)

    for node in nodes:
        if node not in graph:
            graph[node] = []

    return graph

def depth_first_search(root, graph, visited):
    if root not in visited:
        visited.append(root)
        for neighbor in graph[root]:
            depth_first_search(neighbor, graph, visited)
    return visited

def dfs_search(target, graph):
    root = list(graph.keys())[0]
    visited = set()
    result = depth_first_search(root, graph, visited)
    return result

def breadth_first_search(graph, root):
    queue = collections.deque([root])
    visited = set()
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result


def add_edge(start, end, graph):
    graph[start].append(end)
    return graph

def print_graph(graph):
    for x in sorted(graph.keys()):
        print(x, ":", graph[x])

def main():
    graph = create_graph([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)])
    graph = add_edge(3, 5, graph)
    graph = add_edge(0, 2, graph)
    print_graph(graph)
    print(depth_first_search(1, graph, []))
    print(breadth_first_search(graph, 1))

main()
