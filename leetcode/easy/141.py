# 141. Linked List Cycle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head 
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if fast is head:
                return True
        return False
    
node3 = ListNode(3)

node2 = ListNode(2)
node2.next=node3

node1 = ListNode(1)
node1.next=node2

solution = Solution()
print(solution.hasCycle(node1))
