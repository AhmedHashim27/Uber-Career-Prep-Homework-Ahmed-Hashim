'''
# Data Structure: None
# Algorithm: None (Direct generation of binary numbers)
# Time Complexity: O(k)
# Space Complexity: O(1)
#time = 15 mins

def generateBinaryNumbers(k):
    result = []
    for i in range(k):
        result.append(bin(i)[2:])

#    return result

# Test cases
print(generateBinaryNumbers(5))  # Output: ["0", "1", "10", "11", "100"]
print(generateBinaryNumbers(10))  # Output: ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
'''

# Data Structure: Queue
# Algorithm: Breadth-first search (BFS)
# Time Complexity: O(k)
# Space Complexity: O(k)
# Time 35 mis 

from collections import deque

def generateBinaryNumbers(k):
    result = []
    queue = deque()
    queue.append("1")

    for _ in range(k):
        binary_number = queue.popleft()
        result.append(binary_number)

        queue.append(binary_number + "0")
        queue.append(binary_number + "1")

    return ["0"] + result[:-1]  # Add "0" to the front and remove the last element

# Test cases
print(generateBinaryNumbers(5))  # Output: ["0", "1", "10", "11", "100"]
print(generateBinaryNumbers(10))  # Output: ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
