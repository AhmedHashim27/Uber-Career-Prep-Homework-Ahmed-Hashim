
#depth-first search (DFS)
#The time complexity of the code is O(n + m)
#The space complexity is also O(n + m).
# Time = 50 min
from collections import defaultdict

# use dfs to traverse all roads of a town
def dfs(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

# build adjacency list of the graph
def build_graph(edges):
    graph = defaultdict(set)
    for town1, town2 in edges:
        graph[town1].add(town2)
        graph[town2].add(town1)
    return graph

def RoadNetworks(towns, roads):
    if len(roads) == 0:
        return 0
    adjacency_list = build_graph(roads)
    num_of_networks = 0
    visited = set()
    # traverse all towns to find the number of networks
    for town in adjacency_list:
        if town not in visited:
            dfs(adjacency_list, town, visited)
            num_of_networks += 1
    return num_of_networks

def main():
    # Test Case 1
    towns1 = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"]
    roads1 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
    result1 = RoadNetworks(towns1, roads1)
    print("Test Case 1:")
    print(" Output:", result1)

    # Test Case 2
    towns2 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
    roads2 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
    result2 = RoadNetworks(towns2, roads2)
    print("Test Case 2:")
    print(" Output:", result2)


if __name__ == "__main__":
    main()
