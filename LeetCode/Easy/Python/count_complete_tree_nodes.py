# https://leetcode.com/problems/count-complete-tree-nodes/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        def traverse(node: TreeNode):
            nonlocal count
            if node:
                count += 1
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        return count