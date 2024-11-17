# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        values.reverse()

        if len(values) == 1:
            return ListNode(values[0])
        new_head = ListNode(values[0])
        node = ListNode()
        new_head.next = node
        for i in range(1, len(values)):
            node.val = values[i]
            if i != len(values) - 1:
                node.next = ListNode()
            node = node.next
        return new_head
