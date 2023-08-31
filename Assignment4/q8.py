'''
Technique Used: Dynamic Programming (DP)

Time Complexity: The time complexity is O(coins * target_sum) because we use two nested loops, one for coins and one for the target sum.

Space Complexity: The space complexity is O(target_sum) to store the DP array.

'''

def coin_change_combinations(coins, target_sum):
    dp = [0] * (target_sum + 1)
    dp[0] = 1  # There is one way to make change for zero

    for coin in coins:
        for i in range(coin, target_sum + 1):
            dp[i] += dp[i - coin]

    return dp[target_sum]

# Test cases
coins1 = [2, 5, 10]
target_sum1 = 20
print(coin_change_combinations(coins1, target_sum1))  # Output should be 6

coins2 = [2, 5, 10]
target_sum2 = 15
print(coin_change_combinations(coins2, target_sum2))  # Output should be 3
