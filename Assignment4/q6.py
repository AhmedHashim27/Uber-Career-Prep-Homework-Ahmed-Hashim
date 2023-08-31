'''
Technique Used: Dynamic Programming (DP)

Time Complexity: The time complexity is O(n^2) because we use two nested loops to fill the DP array.

Space Complexity: The space complexity is O(n) to store the DP array.

'''

def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always a valid word

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]

# Test cases
word_dict = {"Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"}

input1 = "mangolf"
print(word_break(input1, word_dict))  # Output should be True

input2 = "manateenotelf"
print(word_break(input2, word_dict))  # Output should be True

input3 = "quipig"
print(word_break(input3, word_dict))  # Output should be False
