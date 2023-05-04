class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def top(self):
        if self.head is None:
            return None
        return self.head.val
    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.head is None:
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.val
    
    def is_empty(self):
        return self.head is None
