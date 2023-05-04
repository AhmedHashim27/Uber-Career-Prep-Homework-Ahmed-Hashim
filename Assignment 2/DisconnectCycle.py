'''
Linked List fast-slow two-pointer
Time complexity: O(N)
Space complexity: O(1)
Time: 1 hour
'''
class ListNode:
def init(self, val=0, next=None):
self.val = val
self.next = next

def disconnect_cycle(head: ListNode) -> None:
if not head or not head.next:
return

slow = head
fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        break

if slow != fast:
    return

slow = head
while slow != fast:
    slow = slow.next
    fast = fast.next

while fast.next != slow:
    fast = fast.next

fast.next = None
#Test Cases
#Test Case 1
#The linked list has no cycle
#The function should not modify the list
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

disconnect_cycle(head1)
assert head1.val == 1
assert head1.next.val == 2
assert head1.next.next.val == 3
assert head1.next.next.next.val == 4
assert head1.next.next.next.next.val == 5
assert head1.next.next.next.next.next == None

#Test Case 2
#The linked list has a cycle
#The function should disconnect the cycle
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = head2.next.next

disconnect_cycle(head2)
assert head2.val == 1
assert head2.next.val == 2
assert head2.next.next.val == 3
assert head2.next.next.next.val == 4
assert head2.next.next.next.next == None
