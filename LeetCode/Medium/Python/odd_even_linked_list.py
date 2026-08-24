# https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd = []
        even = []
        node = head
        count = 1
        while node:
            if count % 2 == 0:
                even.append(node.val)
            else:
                odd.append(node.val)
            node = node.next
            count += 1
        return self.combine([*odd, *even])

    def combine(self, values: list[int]) -> ListNode:
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
