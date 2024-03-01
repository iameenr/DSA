# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        avg = []

        q = deque([root])
        while q:
            levelsum, levellen = 0, len(q)
            for i in range(levellen):
                node = q.popleft()
                levelsum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avg.append(levelsum / levellen)
            

        return avg