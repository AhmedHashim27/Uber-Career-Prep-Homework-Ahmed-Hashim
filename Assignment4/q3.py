'''
Technique Used: Maintain two heaps (min-heap and max-heap)

Time Complexity: The time complexity for adding a number is O(log N) since we perform a push and potentially a pop operation on the heaps. Finding the median is O(1) since we only need to peek at the heaps.

Space Complexity: The space complexity is O(N) to store the input numbers in two heaps.

'''

import heapq

class RunningMedian:
    def __init__(self):
        self.min_heap = []  # Stores the larger half of the numbers
        self.max_heap = []  # Stores the smaller half of the numbers

    def add_number(self, num):
        # Add the number to the appropriate heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance the heaps if necessary
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            # Even number of elements, take the average of the two middle elements
            median = (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            # Odd number of elements, the median is the middle element in the max_heap
            median = -self.max_heap[0]
        return median

# Test cases
running_median = RunningMedian()
input_numbers = [1, 11, 4, 15, 12]

for num in input_numbers:
    running_median.add_number(num)
    median = running_median.find_median()
    print(f"Input: {num}, Median: {median}")
