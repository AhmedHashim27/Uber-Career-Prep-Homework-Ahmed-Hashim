# Time Complexity O(n)
# Method: Hash linked list nodes
# 20 Minutes

# Time Complexity O(n)
# Method: Hash linked list nodes
# 20 Minutes

class Node:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        node = self
        while node is not None:
            values.append(node.val)
            node = node.next
        return " -> ".join(str(val) for val in values)

    def deleteNode(self, head, value):
        if head is None:
            return None

        if head.val == value:
            return head.next

        curr = head

        while curr.next is not None:
            if curr.next.val == value:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head
    
    def deup_sorted_list(self, head):
        if head is None:
            return None

        hash = set()
        curr = head
        hash.add(head.val)

        while curr.next is not None:
            if curr.next.val in hash:
                curr.deleteNode(head, curr.next.val)
            else:
                hash.add(curr.next.val)
                curr = curr.next

        return head

# create the linked list: 1 -> 1 -> 2 -> 3 -> 3 -> 4
head = Node(1, Node(1, Node(2, Node(3, Node(3, Node(4))))))
print(head)

# call the method to remove duplicates
head = head.deup_sorted_list(head)

# check that duplicates have been removed: 1 -> 2 -> 3 -> 4
print(head)
