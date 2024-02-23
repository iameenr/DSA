# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(node):  
            result = 0
            if node is not None:
                if low <= node.val <= high:
                    result = node.val
                result += dfs(node.left)
                result += dfs(node.right)
            return result

        return dfs(root)
