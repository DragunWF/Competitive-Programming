# https://leetcode.com/problems/leaf-similar-trees/description/

from collections import deque

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return False
        return self.getLeaves(root1) == self.getLeaves(root2)
    
    def getLeaves(self, root: TreeNode) -> list[int]:
        result = []
    
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                if not node.left and not node.right:
                    result.append(node.val)
    
        traverse(root)
        return result