# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        node = head
        while node != None:
            values.append(node)
            node = node.next
        return values[math.floor(len(values) / 2) if len(values) % 2 != 0 else len(values) // 2]
