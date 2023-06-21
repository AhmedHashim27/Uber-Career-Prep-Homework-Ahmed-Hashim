class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):
        if len(self.arr) == 0:
            raise ValueError("Priority queue is empty")
        return self.arr[0][0]

    def insert(self, x, weight):
        self.arr.append((x, weight))
        self.heapify_up(len(self.arr) - 1)

    def remove(self):
        if len(self.arr) == 0:
            raise ValueError("Priority queue is empty")

        self.swap(0, len(self.arr) - 1)
        self.arr.pop()
        self.heapify_down(0)

    def heapify_up(self, index):
        while index > 0 and self.arr[index][1] > self.arr[(index - 1) // 2][1]:
            self.swap(index, (index - 1) // 2)
            index = (index - 1) // 2

    def heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.arr) and self.arr[left][1] > self.arr[largest][1]:
            largest = left

        if right < len(self.arr) and self.arr[right][1] > self.arr[largest][1]:
            largest = right

        if largest != index:
            self.swap(index, largest)
            self.heapify_down(largest)

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]


def main():
    # Create a priority queue object
    pq = PriorityQueue()

    # Insert elements into the priority queue
    pq.insert('Apple', 3)
    pq.insert('Banana', 2)
    pq.insert('Orange', 1)

    # Print the top element
    print("Top element:", pq.top())  # Output: Top element: Orange

    # Remove the top element
    pq.remove()

    # Print the top element after removal
    print("Top element after removal:", pq.top())  # Output: Top element after removal: Apple

    # Insert a new element
    pq.insert('Grapes', 4)

    # Remove all elements from the priority queue
    while len(pq.arr) > 0:
        pq.remove()

    # Attempt to retrieve the top element from an empty priority queue (raises an exception)
    try:
        print("Top element:", pq.top())
    except ValueError as e:
        print("Error:", str(e))  # Output: Error: Priority queue is empty


if __name__ == "__main__":
    main()
