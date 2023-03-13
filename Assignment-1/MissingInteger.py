"""
Ahmed Hashim
02-25-2023
MissingInteger:
Given an integer n and a sorted array of integers of size n-1 which contains all but one of the integers in the range 1-n, find the missing integer.

Time Complexity: O(n log n)

Space Complexity: O(1)

Technique: Sorting algorithm variation


Time Spent:
roughly 20 minutes

Approach:

1) Sort the given array in ascending order.
2) If the first element of the array is not 1, then 1 is missing. Return 1.
3) If the last element of the array is not n, then n is missing. Return n.
4) Iterate through the array from the second element to the second to last element.
5) If the difference between the current element and the previous element is greater than 1, then the missing integer is between the two elements. Return the previous element plus 1.
6) If no missing integer is found, return None or any other value that represents the absence of a value.
"""

def find_missing_integer(arr, n):
    arr.sort()
    if arr[0] != 1:
        return 1

    if arr[-1] != n:
        return n

    for i in range(1, n-1):
        if arr[i] - arr[i-1] != 1:
            return arr[i] - 1

    return None



#Test cases
assert find_missing_integer([1, 2, 3, 4, 6, 7], 7) == 5
assert find_missing_integer([1], 2) == 2
assert find_missing_integer([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12) == 9
assert find_missing_integer([2, 3, 4, 5, 6, 7, 8, 9], 10) == 1

