# https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for head in lists:
            for num in self.flatten(head):
                values.append(num)
        values.sort()
        return self.convert_to_linked_list(values)

    def flatten(self, head: ListNode) -> List[int]:
        values = []
        node = head
        while node != None:
            values.append(node.val)
            node = node.next
        return values

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
