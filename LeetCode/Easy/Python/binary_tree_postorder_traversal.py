# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        def traverse(node: TreeNode):
            if node:
                traverse(node.left)
                traverse(node.right)
                values.append(node.val)
        traverse(root)
        return values