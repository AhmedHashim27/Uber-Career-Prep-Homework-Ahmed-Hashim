'''
Technique Used: Dynamic Programming (DP)

Time Complexity: The time complexity of generating Catalan numbers from 0 to n using dynamic programming is O(n^2).

Space Complexity: The space complexity is O(n) to store the Catalan numbers.
'''

def generate_catalan_numbers(n):
    if n < 0:
        return []

    catalan = [0] * (n + 1)
    catalan[0] = 1

    for i in range(1, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]

    return catalan

# Test cases
n = 5
catalan_numbers = generate_catalan_numbers(n)
print(catalan_numbers)  # Output should be [1, 1, 2, 5, 14, 42]
