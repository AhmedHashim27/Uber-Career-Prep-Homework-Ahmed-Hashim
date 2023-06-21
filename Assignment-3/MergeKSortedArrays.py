'''
Data Structure: Heap
Algorithm: Merge K Sorted Arrays

Time Complexity: O(N log K), where N is the total number of elements across all arrays and K is the number of arrays.
Space Complexity: O(N), where N is the total number of elements across all arrays.
Time 25 mins
'''

import heapq


def merge_k_sorted_arrays(k, arrays):
    # Create a min-heap to store the elements
    heap = []
    result = []

    # Initialize the heap with the first element from each array
    for i in range(k):
        if len(arrays[i]) > 0:
            heapq.heappush(heap, (arrays[i][0], i, 0))

    # Merge the arrays using the heap
    while heap:
        element, array_index, index = heapq.heappop(heap)
        result.append(element)

        # Move to the next element in the array
        if index + 1 < len(arrays[array_index]):
            next_element = arrays[array_index][index + 1]
            heapq.heappush(heap, (next_element, array_index, index + 1))

    return result


# Test cases
input_k = 2
input_arrays = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
print(merge_k_sorted_arrays(input_k, input_arrays))  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

input_k = 3
input_arrays = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
print(merge_k_sorted_arrays(input_k, input_arrays))  # Output: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]
