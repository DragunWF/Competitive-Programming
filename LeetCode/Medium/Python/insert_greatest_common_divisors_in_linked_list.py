# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        node = head
        prev = node.val
        while node:
            if values:
                values.append(gcd(prev, node.val))
            values.append(node.val)
            prev = node.val
            node = node.next
        return self.to_linked_list(values)

    def to_linked_list(self, values: List[int]) -> ListNode:
        if not values:
            return None
        head = ListNode(values[0])
        if len(values) == 1:
            return head
        node = ListNode()
        head.next = node
        for i in range(1, len(values)):
            node.val = values[i]
            if i != len(values) - 1:
                node.next = ListNode()
            node = node.next
        return head
