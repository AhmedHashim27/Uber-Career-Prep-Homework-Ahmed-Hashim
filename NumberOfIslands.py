# Data Structure: Graph (Adjacency Matrix or Adjacency List)
# Algorithm: Depth-first search (DFS)
# Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the binary matrix.
# Space Complexity: O(1)
# time = 40 min

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] <= 0:
        return
    grid[i][j] = -1
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)

def numIslands(grid):
    if not grid:
        return 0
    
    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                num_islands += 1
                dfs(grid, i, j)
    
    return num_islands

# Test cases
grid1 = [
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
print(numIslands(grid1))  # Output: 3

grid2 = [
        [1, 0, 0],
        [0, 0, 0]
    ]
print(numIslands(grid2))  # Output: 1
