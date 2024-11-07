# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None and list2:
            return list2
        if list1 and list2 is None:
            return list1
        first_list = self.get_values(list1)
        second_list = self.get_values(list2)

        sorted_list = sorted([*first_list, *second_list])
        head = ListNode(sorted_list[0])
        current = ListNode()
        head.next = current
        for i in range(1, len(sorted_list)):
            current.val = sorted_list[i]
            if i != len(sorted_list) - 1:
                current.next = ListNode()
                current = current.next

        return head

    def get_values(self, node: ListNode) -> list[int]:
        values = []
        while node != None:
            values.append(node.val)
            node = node.next
        return values
