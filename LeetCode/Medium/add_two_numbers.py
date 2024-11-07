# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = int(self.str_num(l1)[::-1]) + int(self.str_num(l2)[::-1])
        values = [int(n) for n in str(total)]
        values.reverse()
        head = ListNode(values[0])
        if len(values) > 1:
            current = ListNode()
            head.next = current
            for i in range(1, len(values)):
                current.val = values[i]
                if i != len(values) - 1:
                    current.next = ListNode()
                    current = current.next
        return head

    def str_num(self, node: ListNode) -> str:
        output = ""
        current = node
        while current != None:
            output += str(current.val)
            current = current.next
        return output
