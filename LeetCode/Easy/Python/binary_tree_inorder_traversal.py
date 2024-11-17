# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        def traverse(node: TreeNode):
            if node:
                traverse(node.left)
                values.append(node.val)
                traverse(node.right)
        traverse(root)
        return values
