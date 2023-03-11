"""
Ahmed Hashim
02-17-2023
MaxMeanSubArray:
Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.

Time complexity: O(n), where n is the length of the input array. We only need to iterate over the input array once.
Space complexity: O(1), as we only use a constant amount of extra space to store variables.

Technique:
Fixed-Size Sliding Window

Time Spent:
40 minutes

Approach:

1)Check if k is greater than the length of the input array. If it is, return None since it is impossible to have a subarray of size k.

2)Initialize two variables: max_sum to store the maximum sum seen so far, and current_sum to store the sum of the current subarray of size k (i.e., the first k elements of the array).

3)Iterate over the array from index k to the end of the array:

Add the current element to the current_sum and subtract the element k positions to the left of it.
Update max_sum to be the maximum of max_sum and current_sum.

4)Return max_sum divided by k to get the maximum mean of a subarray of size k.
"""

def max_mean_subarray(arr, k):
    n = len(arr)
    if k > n:
        return None

    curr_sum = sum(arr[:k])
    max_sum = curr_sum

    for i in range(k, n):
        curr_sum += arr[i] - arr[i-k]
        # I have searched for that line because I didn't know how to substarct the privious element
        max_sum = max(max_sum, curr_sum)


    return max_sum / k 

assert max_mean_subarray([4, 5, -3, 2, 6, 1], 2) == 4.5
assert max_mean_subarray([4, 5, -3, 2, 6, 1], 3) == 3
assert max_mean_subarray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3) == 1
assert max_mean_subarray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5) == 1





