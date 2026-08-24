# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique = set()
        duplicates = set()
        node = head
        while node:
            if not node.val in unique and not node.val in duplicates:
                unique.add(node.val)
            else:
                duplicates.add(node.val)
                unique.discard(node.val)
            node = node.next
        return self.convert_to_linked_list(sorted(list(unique)))
    
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