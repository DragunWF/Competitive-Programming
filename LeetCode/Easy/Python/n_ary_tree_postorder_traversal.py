# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        values = []
        def traverse(node):
            if node:
                for child in node.children:
                    traverse(child)
                values.append(node.val)
        traverse(root)
        return values