"""
Ahmed Hashim
02-25-2023
MergeIntervals:
Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list in which overlapping intervals are merged.

Time Complexity: O(nlogn), where n is the number of intervals

Space Complexity: O(n), where n is the number of intervals

Technique: Sorting and Merging Overlapping Intervals


Time Spent:
roughly 50 minutes

Approach:

1) Check if the length of both strings is the same. If not, return False.
2) Create an array of size 26 to keep track of the frequency count of each character in the first string.
3) Iterate over the characters in the first string and increment the frequency count of each character in the array.
4) Initialize a negative frequency count to 0.
5) Iterate over the characters in the second string and decrement the frequency count of each character in the array.
6) If the frequency count becomes negative, increment the negative frequency count.
7) If the negative frequency count exceeds k, return False.
8) If the loop completes, return True.
"""
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda a : a[0])

    # Merge overlapping intervals
    res = [list(intervals[0])]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(intervals[i][1], res[-1][1])
        else:
            res.append(list(intervals[i]))

    # Convert list back to tuple
    for i in range(len(res)):
        res[i] = tuple(res[i])

    return res

# Test cases
assert merge_intervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]) == [(1, 3), (4, 8), (9, 12)]
assert merge_intervals([(5, 8), (6, 10), (2, 4), (3, 6)]) == [(2, 10)]
assert merge_intervals([(10, 12), (5, 6), (7, 9), (1, 3)]) == [(1, 3), (5, 6), (7, 9), (10, 12)]
assert merge_intervals([]) == []
assert merge_intervals([(1, 2)]) == [(1, 2)]


