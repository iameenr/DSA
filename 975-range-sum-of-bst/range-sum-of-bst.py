
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

                elif node.val < low:
                    return dfs(node.right)
                elif node.val > high:
                    return dfs(node.left)
                    
            return result
        return dfs(root)