'''
Technique Used: Dynamic Programming (DP)

Time Complexity: The time complexity of this dynamic programming solution is O(n) because we iterate through the array once.

Space Complexity: The space complexity is O(n) to store the DP array.

'''

def min_cost_stair_climbing(cost):
    n = len(cost)
    if n <= 1:
        return 0

    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[-1], dp[-2])

# Test cases
cost1 = [4, 1, 6, 3, 5, 8]
print(min_cost_stair_climbing(cost1))  # Output should be 9

cost2 = [11, 8, 3, 4, 9, 13, 10]
print(min_cost_stair_climbing(cost2))  # Output should be 25
