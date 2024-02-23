# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(node):  
            if node is None:
                return
            if low <= node.val <= high:
                global result
                result += node.val
            dfs(node.left)
            dfs(node.right)

        global result
        result = 0
        dfs(root)
        return result
