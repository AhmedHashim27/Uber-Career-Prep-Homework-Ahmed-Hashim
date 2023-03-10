def max_mean_subarray(arr, k):
    n = len(arr)
    if k > n:
        return None

    curr_sum = sum(arr[:k])
    max_sum = curr_sum

    for i in range(k, n):
        curr_sum += arr[i] - arr[i-k]
        # i have searched for that line because I didn't know how to substarct the privious element
        max_sum = max(max_sum, curr_sum)


    return(max_sum / k) 

assert max_mean_subarray([4, 5, -3, 2, 6, 1], 2) == 4.5
assert max_mean_subarray([4, 5, -3, 2, 6, 1], 3) == 3
assert max_mean_subarray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3) == 1
assert max_mean_subarray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5) == 1
