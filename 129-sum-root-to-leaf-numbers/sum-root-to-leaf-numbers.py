class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def _sumNumbers(node, prefix):
            if not node.left and not node.right: #leaf
                self.total_sum += ((prefix*10) + node.val)
                return
            
            prefix = (prefix*10) + node.val
            node.left  and _sumNumbers(node.left, prefix)
            node.right and _sumNumbers(node.right, prefix) 
            return

        self.total_sum = 0
        _sumNumbers(root, 0)
        return self.total_sum
        