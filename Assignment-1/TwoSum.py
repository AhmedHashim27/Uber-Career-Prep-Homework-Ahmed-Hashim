"""
Ahmed Hashim
03-12-2023
TwoSum:
Given an array of integers and a target integer, k, return the number of pairs of integers in the array that sum to k. In each pair, the two items must be distinct elements (come from different indices in the array).


Time complexity: O(n)

Space complexity: O(n)

Technique: Hashing Technique - One-directional running computation/total


Time Spent:
roughly 30 minutes

Approach:
Step 1: Initialize a count variable to 0.

Step 2: Create an empty dictionary called num_counts.

Step 3: Loop through the input array arr, and for each element num in arr, do the following:
If num is already a key in num_counts, increment its corresponding value by 1.
If num is not a key in num_counts, add it to num_counts with a value of 1.

Step 4: Loop through the keys of num_counts, and for each key num, do the following:
Calculate the complement of num as k - num.
If the complement is a key in num_counts and it is not equal to num, then add the product of the values of num_counts[num] and num_counts[complement] to count.

Step 5: Return count divided by 2, since each pair of elements is counted twice (once for each of the two elements).
# confused about test case #2, there are 3 pairs in the example but the output is 4?

"""

def count_pairs_with_sum_k(arr, k):
    count = 0
    num_counts = {}
    for num in arr:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    for num in num_counts:
        complement = k - num
        if complement in num_counts and complement != num:
            count += num_counts[num] * num_counts[complement]

    if k % 2 == 0 and k // 2 in num_counts:
        count -= num_counts[k // 2] // 2

    return count // 2



assert count_pairs_with_sum_k([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10) == 3
assert count_pairs_with_sum_k([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 8) == 4   
assert count_pairs_with_sum_k([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6) == 5
assert count_pairs_with_sum_k([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1) == 0

'''
# Test Cases
arr1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
k1 = 10
print(count_pairs_with_sum_k(arr1, k1)) # Output: 3

arr2 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
k2 = 8
print(count_pairs_with_sum_k(arr2, k2)) # Output: 4 but it gives me 3

arr3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
k3 = 6
print(count_pairs_with_sum_k(arr3, k3)) # Output: 5

arr4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
k4 = 1
print(count_pairs_with_sum_k(arr4, k4)) # Output: 0
'''
