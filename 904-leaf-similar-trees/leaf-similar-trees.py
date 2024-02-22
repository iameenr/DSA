# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, roota: Optional[TreeNode], rootb: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.left is None and node.right is None:
                ls.append(node.val)
            if node.left:  dfs(node.left)
            if node.right: dfs(node.right)


        ls = []
        dfs(roota)
        lsa = ls

        ls = []
        dfs(rootb)
        lsb = ls
        return lsa == lsb