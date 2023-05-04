'''
Doubly linked list forward-backward two-pointer
Time complexity: O(N), 
space complexity: O(1)
Time: 40
'''
class ListNode:
def init(self, val=0, prev=None, next=None):
self.val = val
self.prev = prev
self.next = next

def is_palindrome(head: ListNode) -> bool:
if not head or not head.next:
return True
left = head
right = head
while right.next:
    right = right.next

while left != right and right.next != left:
    if left.val != right.val:
        return False
    left = left.next
    right = right.prev

return True

#Test Cases
#Example 1
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
assert is_palindrome(head) == True

#Example 2
head = ListNode(1, ListNode(2))
assert is_palindrome(head) == False

#Example 3
head = ListNode(1)
assert is_palindrome(head) == True

#Example 4
head = None
assert is_palindrome(head) == True
