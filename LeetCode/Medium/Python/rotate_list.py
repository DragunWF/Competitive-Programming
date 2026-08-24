# https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        rotated = [None for i in range(len(values))]
        for i in range(len(values)):
            rotated[(i + k) % len(values)] = values[i]
        return self.convert_to_linked_list(rotated)

    def convert_to_linked_list(self, values: List[int]) -> ListNode:
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
