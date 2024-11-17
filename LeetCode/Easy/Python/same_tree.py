# https://leetcode.com/problems/same-tree/


from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print(self.getNodeValues(p), self.getNodeValues(q))
        return self.getNodeValues(p) == self.getNodeValues(q)

    def getNodeValues(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        return result
