def TwoSum(arr,k):

    dict_with_arr_elements = {}
    total_count = 0
    for num in arr:
        if num in dict_with_arr_elements:
            dict_with_arr_elements[num] += 1
        else:
            dict_with_arr_elements[num] = 1

    for num in arr:

        if k - num in dict_with_arr_elements:
            total_count += dict_with_arr_elements[k-num]

            if k-num == num:
                total_count -= 1

    return total_count//2


assert TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10) == 3
assert TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 8) == 3   
assert TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6) == 5
assert TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1) == 0