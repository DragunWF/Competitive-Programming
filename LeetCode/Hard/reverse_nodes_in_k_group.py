# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = self.get_values_in_groups(head, k)
        for i in range(len(values)):
            if len(values[i]) == k:
                values[i] = reversed(values[i])
        return self.convert_to_linked_list(self.flatten_list(values))
    
    def flatten_list(self, values: List[int]) -> List[int]:
        output = []
        for arr in values:
            for num in arr:
                output.append(num)
        return output
    
    def get_values_in_groups(self, head: ListNode, k: int) -> List[int]:
        values = []
        group = []
        count = 0
        node = head

        while node:
            count += 1
            group.append(node.val)
            if count % k == 0:
                values.append(group)
                group = []
            node = node.next
        if group:
            values.append(group)

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
