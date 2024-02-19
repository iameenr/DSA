class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node is None:
                return 

            preorder.append(node.val)
            dfs(node.left)
            dfs(node.right)

        preorder = []
        dfs(root)
        return preorder