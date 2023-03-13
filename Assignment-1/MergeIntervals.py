"""
Ahmed Hashim
02-25-2023
MergeIntervals:
Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list in which overlapping intervals are merged.

Time Complexity: O(nlogn), where n is the number of intervals

Space Complexity: O(n), where n is the number of intervals

Technique: Sorting and Merging Overlapping Intervals


Time Spent:
roughly 80 minutes

Approach:

1) Check the input list of intervals for empty or None input. If the list is empty or None, return an empty list.
2) Sort the input list of intervals based on their start times. This will help in detecting and merging overlapping intervals in the next step.
3) Initialize an empty list to store the merged intervals.
4) Iterate through the sorted input list of intervals, starting from the second interval (i.e., intervals[1:]) to compare it with the previous interval.
5) If the start time of the current interval is less than or equal to the end time of the previous interval, it means the two intervals overlap. In this case, merge the two intervals by updating the end time of the previous interval with the maximum of its current end time and the end time of the current interval.
6) If the start time of the current interval is greater than the end time of the previous interval, it means the two intervals do not overlap. In this case, add the current interval to the list of merged intervals.
7) After iterating through all intervals, return the list of merged intervals.
"""
def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda a : a[0])

    res = [list(intervals[0])]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(intervals[i][1], res[-1][1])
        else:
            res.append(list(intervals[i]))

    for i in range(len(res)):
        res[i] = tuple(res[i])

    return res


# Test cases
assert merge_intervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]) == [(1, 3), (4, 8), (9, 12)]
assert merge_intervals([(5, 8), (6, 10), (2, 4), (3, 6)]) == [(2, 10)]
assert merge_intervals([(10, 12), (5, 6), (7, 9), (1, 3)]) == [(1, 3), (5, 6), (7, 9), (10, 12)]
assert merge_intervals([]) == []
assert merge_intervals([(1, 2)]) == [(1, 2)]


