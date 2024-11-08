# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        values = []
        node = head
        count = 0
        while node != None:
            values.append(node.val)
            node = node.next
            count += 1

        values.pop(count - n)
        if not values:
            return None
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
