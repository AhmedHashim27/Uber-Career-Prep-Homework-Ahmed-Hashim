'''
Technique Used: Dynamic Programming (DP)

Time Complexity: The time complexity is O(rows * cols) because we iterate through the entire matrix once.

Space Complexity: The space complexity is O(rows * cols) to store the DP array.

'''
def largest_square_of_ones(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side_length = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side_length = max(max_side_length, dp[i][j])

    return max_side_length

# Test cases
matrix1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]
print(largest_square_of_ones(matrix1))  # Output should be 2

matrix2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0]
]
print(largest_square_of_ones(matrix2))  # Output should be 3

