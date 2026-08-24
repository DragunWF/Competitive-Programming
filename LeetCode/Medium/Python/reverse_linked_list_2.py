# https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        values = []
        node = head
        index = 0
        while node:
            values.append(node.val)
            node = node.next
        
        reverse = list(reversed(values[left - 1:right]))
        j = 0
        for i in range(len(values)):
            if (left - 1) <= i < right:
                print(reverse, reverse[j], j)
                values[i] = reverse[j]
                j += 1
        return self.convert_to_linked_list(values)
    
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