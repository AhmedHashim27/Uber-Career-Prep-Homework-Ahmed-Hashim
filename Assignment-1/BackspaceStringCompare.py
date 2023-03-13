"""
Ahmed Hashim
02-19-2023
BackspaceStringCompare:
Given two strings representing series of keystrokes, determine whether the resulting 
text is the same. Backspaces are represented by the '#' character so "x#" results in the 
empty string ("").

Time Complexity: O(n), where n is the length of the longer string

Space Complexity: O(1), constant space usage

Technique: Two Pointer Techniques: Forward/backward two-pointer


Time Spent:
roughly 40 minutes

Approach:

1)Initialize two pointers i and j to the end of both strings s1 and s2, respectively.

2)Initialize two variables backspace_count1 and backspace_count2 to zero.

3)While i or j is greater than or equal to zero, do the following:
a. Move the pointers i and j to the index of the character before the '#' character (if any) in s1 and s2, respectively. To do this, use a while loop to skip any '#' characters and decrement the corresponding backspace count. Stop when a non-'#' character is encountered or both pointers reach the beginning of their respective strings.
b. If either pointer has reached the beginning of its string, return whether both pointers are at the same index (i.e., i == j).
c. If the characters at the current indices of s1 and s2 are not the same, return False.
d. Decrement both pointers by 1.

4)Return True.

"""

def is_same_text(s1: str, s2: str) -> bool:
    i = len(s1) - 1 # pointer for s1
    j = len(s2) - 1 # pointer for s2
    backspace_count1 = backspace_count2 = 0

    while i >= 0 or j >= 0:
        # find the index of the character before '#' in s1
        while i >= 0 and (s1[i] == '#' or backspace_count1 > 0):
            if s1[i] == '#':
                backspace_count1 += 1
            else:
                backspace_count1 -= 1
            i -= 1
        # find the index of the character before '#' in s2
        while j >= 0 and (s2[j] == '#' or backspace_count2 > 0):
            if s2[j] == '#':
                backspace_count2 += 1
            else:
                backspace_count2 -= 1
            j -= 1
        
        # if either string is finished
        if i < 0 or j < 0:
            return i == j
        
        if s1[i] != s2[j]:
            return False
        
        i -= 1
        j -= 1

    return True

#Test cases
assert is_same_text("abcde", "abcde") == True
assert is_same_text("Uber Career Prep", "u#Uber Careee#r Prep") == True
assert is_same_text("abcdef###xyz", "abcw#xyz") == True
assert is_same_text("abcdef###xyz", "abcdefxyz###") == False

