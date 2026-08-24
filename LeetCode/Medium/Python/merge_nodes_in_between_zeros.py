# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        node = head
        in_between = []
        while node:
            if node.val == 0:
                if in_between:
                    values.append(in_between)
                in_between = []
            else:
                in_between.append(node.val)
            node = node.next
        return self.to_linked_list([sum(arr) for arr in values])

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
