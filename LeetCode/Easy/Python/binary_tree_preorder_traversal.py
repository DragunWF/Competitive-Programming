# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        def traverse(node: TreeNode):
            if node:
                values.append(node.val)
                traverse(node.left)
                traverse(node.right)
        traverse(root)
        return values