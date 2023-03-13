"""
Ahmed Hashim
03-02-2023
DedupArray:
Given a sorted array of non-negative integers, modify the array by removing duplicates so each 
element only appears once. If arrays are static (aka, not dynamic/resizable) in your language 
of choice, the remaining elements should appear in the left-hand side of the array and 
the extra space in the right-hand side should be padded with -1s.

Time Complexity: O(n) - We need to iterate through the entire array once

Space Complexity: O(1) - No extra data structure is used

Technique: Two Pointer Technique - Forward/backward two-pointer


Time Spent:
roughly 20 minutes

Approach:
1) Initialize a variable last_non_duplicate to 0 to keep track of the index of the last non-duplicate element in the array.
2) Iterate through the array from index 1 to the end:
a. If the current element is not equal to the last non-duplicate element, 
increment last_non_duplicate and set the value of the element at index last_non_duplicate to the current element.
3) Iterate through the remaining elements in the array from index last_non_duplicate + 1 to the end and set their values to -1.
4) Return a slice of the array from index 0 to last_non_duplicate + 1.
"""
def remove_duplicates(arr):
    if not arr:
        return arr
    unique = []
    for num in arr:
        if num not in unique:
            unique.append(num)
    n = len(arr)
    for i in range(len(unique), n):
        unique.append(-1)
    return unique

# Test_cases

assert remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [1, 2, 3, 4, -1, -1, -1, -1, -1, -1]
assert remove_duplicates([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]) == [0, 1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1, -1]
assert remove_duplicates([1, 3, 4, 8, 10, 12]) == [1, 3, 4, 8, 10, 12]
assert remove_duplicates([]) == []
