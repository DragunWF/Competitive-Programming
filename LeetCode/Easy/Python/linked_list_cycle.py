# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        node = head
        while node:
            if node in seen:
                return True
            seen.append(node)
            node = node.next
        return False