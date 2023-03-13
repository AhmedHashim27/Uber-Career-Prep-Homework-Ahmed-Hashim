"""
Ahmed Hashim
02-20-2023
ShortestSubstring:
Given a string and a second string representing required characters,
 return the length of the shortest substring containing all the required characters.

Time Complexity: O(n)

Space Complexity: O(k), where k is the number of required characters

Time Spent:
roughly 60 minutes

Technique: Fixed-size sliding window


Approach:

1) Create a dictionary required_chars to store the count of required characters in string t. Loop through each character in string t, and update the count of each character in required_chars.

2) Initialize two pointers left and right to the start of the string s, and a variable count to the length of required_chars.

3) Use a while loop to iterate through the string s until the right pointer reaches the end of the string.

4) If the character at the right pointer right is in the dictionary required_chars, decrement its count in the dictionary. If the count of the character in the dictionary becomes zero, decrement the count variable.

5) Use another while loop to iterate through the string s until the count variable becomes zero. This means that we have found a substring that contains all the required characters in t.

6) Calculate the length of the substring between the left and right pointers, and update the value of min_len if the new length is shorter than the previous min_len.

7) If the character at the left pointer left is in the dictionary required_chars, increment its count in the dictionary. If the count of the character in the dictionary becomes greater than zero, increment the count variable.

8) Increment the left pointer to slide the window to the right.

Continue iterating through the string s until the right pointer reaches the end of the string.

If the min_len variable has not been updated, return 0, indicating that no substring of s contains all characters of t. Otherwise, return the value of min_len.
"""
def shortest_substring(s: str, t: str) -> int:
    # create a dictionary to store the count of required characters
    required_chars = {}
    for char in t:
        required_chars[char] = required_chars.get(char, 0) + 1
        
    left = 0
    right = 0
    count = len(required_chars)
    min_len = float('inf')

    while right < len(s):

        if s[right] in required_chars:
            required_chars[s[right]] -= 1
            if required_chars[s[right]] == 0:
                count -= 1

        while count == 0:

            min_len = min(min_len, right - left + 1)

            if s[left] in required_chars:
                required_chars[s[left]] += 1
                if required_chars[s[left]] > 0:
                    count += 1
            left += 1
        right += 1
    if min_len == float('inf'):
        return 0
    else:
        return min_len


# Test Cases
assert shortest_substring("abracadabra", "abc") == 4
assert shortest_substring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx") == 10
assert shortest_substring("dog", "god") == 3



