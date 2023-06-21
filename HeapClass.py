class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
        if len(self.arr) == 0:
            raise ValueError("Heap is empty")
        return self.arr[0]

    def insert(self, x):
        self.arr.append(x)
        self.heapify_up(len(self.arr) - 1)

    def remove(self):
        if len(self.arr) == 0:
            raise ValueError("Heap is empty")

        self.swap(0, len(self.arr) - 1)
        self.arr.pop()
        self.heapify_down(0)

    def heapify_up(self, index):
        while index > 0 and self.arr[index] < self.arr[(index - 1) // 2]:
            self.swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def heapify_down(self, index):
        i = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.arr) and self.arr[left] < self.arr[i]:
            i = left
        if right < len(self.arr) and self.arr[right] < self.arr[i]:
            i = right

        if i != index:
            self.swap(index, i)
            self.heapify_down(i)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        
    # Create a new instance of the Heap class
heap = Heap()

# Insert elements into the heap
heap.insert(5)
heap.insert(2)
heap.insert(8)
heap.insert(1)
heap.insert(10)

# Print the top (minimum) element
print(heap.top())  # Output: 1

# Remove the top (minimum) element
heap.remove()

# Print the new top element after removal
print(heap.top())  # Output: 2

# Insert a new element
heap.insert(3)

# Print the top element again
print(heap.top())  # Output: 2

# took 25 mins 
