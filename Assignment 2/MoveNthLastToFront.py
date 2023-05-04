'''
Technique: Linked List Two-Pointer Techniques - Linked List Fast-Slow Two-Pointer
Time: 50min
Time complexity: O(n)
Space complexity: O(1)
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def moveNthLastToFront(head: ListNode, n: int) -> ListNode:
    if not head or not head.next:
        return head

    slow = head
    fast = head

    for i in range(n):
        if not fast.next:
            return head
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    prev = None
    curr = head
    while curr != slow:
        prev = curr
        curr = curr.next

    prev.next = prev.next.next
    curr.next = head
    head = curr

    return head


# Test Cases
def main():
    # Test Case 1
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    head = moveNthLastToFront(node1, 2)
    assert head.val == 4
    assert head.next.val == 1
    assert head.next.next.val == 2
    assert head.next.next.next.val == 3
    assert head.next.next.next.next.val == 5
    assert head.next.next.next.next.next is None

    # Test Case 2
    node4 = ListNode(1)
    node3 = ListNode(2, node4)
    node2 = ListNode(3, node3)
    node1 = ListNode(4, node2)

    head = moveNthLastToFront(node1, 4)
    assert head.val == 1
    assert head.next.val == 4
    assert head.next.next.val == 2
    assert head.next.next.next.val == 3
    assert head.next.next.next.next is None
