from collections import defaultdict, deque

def vacationDestinations(origin, k, edges):
    # Create adjacency list
    neighbors = defaultdict(list)
    for start, end, weight in edges:
        neighbors[start].append((end, weight))
        neighbors[end].append((start, weight))
    
    cities = []
    ncities = 0


    # perform BFS and keep track of time "distance"
    visited = set()
    q = deque()
    q.appendleft((origin, -1))  # queue stores city and distance from origin, origin is -1 because no wait time for start location
    visited.add(origin)
    while q:
        city, distance = q.pop()
        if distance < k:
            ncities += 1
            cities.append(city)
            for ncity, ndistance in neighbors[city]:
                if ncity not in visited:
                    q.appendleft((ncity, ndistance + 1 + distance))  # append (cityname, new distance + 1 (wait time))
                    visited.add(ncity)
        elif distance == k:  # if reached maximum time, append city and no more search
            ncities += 1
            cities.append(city)
        else:
            pass
    return ncities - 1, cities[1:]  # exclude origin city


# Test cases
edges = [
    ("Boston", "New York", 4),
    ("New York", "Philadelphia", 2),
    ("Boston", "Newport", 1.5),
    ("Washington, D.C.", "Harper's Ferry", 1),
    ("Boston", "Portland", 2.5),
    ("Philadelphia", "Washington, D.C.", 2.5)
]

# Test case 1
origin = "New York"
k = 5
output = vacationDestinations(origin, k, edges)
print("case 1:", output[1])

# Test case 2
origin = "New York"
k = 7
output = vacationDestinations(origin, k, edges)
print("case 2:", output[1])

# Test case 3
origin = "New York"
k = 8
output = vacationDestinations(origin, k, edges)
print("case 3:", output[1])
