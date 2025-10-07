# Definition for a binary tree grandparent.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.result = 0

        def dfs(grandparent, parent):
            if parent is None:
                return

            if grandparent.val % 2 == 0:
                if parent.left:
                    self.result += parent.left.val
                if parent.right:
                    self.result += parent.right.val
                    
            dfs(parent, parent.left)
            dfs(parent, parent.right)

        dfs(root, root.left)
        dfs(root, root.right)
        return self.result