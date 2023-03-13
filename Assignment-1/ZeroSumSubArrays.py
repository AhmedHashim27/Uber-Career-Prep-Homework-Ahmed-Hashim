"""
Ahmed Hashim
02-17-2023
ZeroSumSubArrays:
Given an array of integers, count the number of subarrays that sum to zero.

Time complexity: O(n), where n is the length of the input array. 
We need to iterate through the input array once, performing constant time operations for each element.

Space complexity: O(n), where n is the length of the input array. In the worst case, 
all elements in the input array could be distinct, so we need to store them all in the hash table.

Technique: Hashing Techniques (One-directional running computation/total)

Time Spent:
roughly 20 minutes

Approach:

1) Initialize a variable count to 0 to keep track of the number of subarrays that sum to zero.

2) Initialize a variable sum_so_far to 0 to keep track of the running sum of the elements seen so far.

3) Create a dictionary sum_counts with an initial key-value pair of 0:1 to keep track of the count of each running sum seen so far. This initial pair is added because when the running sum is 0, we have found a subarray that sums to 0.

4) Iterate through the input array arr.

5) Add the current element to sum_so_far.

6) If sum_so_far is already in sum_counts, it means there is a subarray that sums to 0 that ends at the current index. Increment the count by the value of sum_counts[sum_so_far] and update sum_counts[sum_so_far] by adding 1 to it.
7) If sum_so_far is not in sum_counts, add it to sum_counts with an initial value of 1.

8)Return the count of subarrays that sum to 0.

"""

def count_zero_sum_subarrays(arr):
	count = 0
	sum_so_far = 0
	sum_counts = {0: 1} # A dictionary to store the count of running sum so far.
	for num in arr:
	    sum_so_far += num
	    if sum_so_far in sum_counts:
	        count += sum_counts[sum_so_far]
	        sum_counts[sum_so_far] += 1
	    else:
	        sum_counts[sum_so_far] = 1

	return count
'''
#Test Cases
assert count_zero_sum_subarrays([4, 5, 2, -1, -3, -3, 4, 6, -7]) == 2
assert count_zero_sum_subarrays([1, 8, 7, 3, 11, 9]) == 0
assert count_zero_sum_subarrays([8, -5, 0, -2, 3, -4]) == 2
assert count_zero_sum_subarrays([]) == 0
assert count_zero_sum_subarrays([0]) == 1
assert count_zero_sum_subarrays([0,0,0]) == 6
'''









