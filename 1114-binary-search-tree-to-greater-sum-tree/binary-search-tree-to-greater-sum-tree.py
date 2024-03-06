class Solution:
    def __init__(self):
        self.greater_sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reversed_inorder(root):
            if root is None: 
                return

            reversed_inorder(root.right)
            self.greater_sum = self.greater_sum + root.val
            root.val = self.greater_sum
            reversed_inorder(root.left)

        reversed_inorder(root)
        return root