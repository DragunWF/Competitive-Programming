# https://leetcode.com/problems/sort-list/description/

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        return self.convert_to_linked_list(sorted(values))
    
    def convert_to_linked_list(self, values: List[int]) -> List[int]:
        if not values:
            return None
        head = ListNode(values[0])
        n = len(values)
        if n == 1:
            return head
        node = ListNode()
        head.next = node
        for i in range(1, n):
            node.val = values[i]
            if i != n - 1:
                node.next = ListNode()
            node = node.next
        return head