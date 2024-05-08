from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        lot = []
        # bfs
        q = deque([root]) 
        while q:
            level = []
            levellen = len(q)

            for _ in range(levellen):
                node = q.popleft()

                level.append(node.val)

                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)

            lot.append(level)
            
        return lot