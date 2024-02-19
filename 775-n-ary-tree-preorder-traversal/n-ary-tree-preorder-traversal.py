"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if node is None:
                return
            preorder.append(node.val)
            for child in node.children:
                dfs(child)


        preorder = []
        dfs(root)
        return preorder