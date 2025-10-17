class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []

        result = []
        q = [root]; levellen = 1
        #reverse level order on alternate iterations
        forward = True
        while q:
            level = []
            for i in range(0, levellen):
                node = q.pop(0) 
                if node:        
                    level.append(node.val)
                    if node.left:  q.append(node.left) 
                    if node.right: q.append(node.right)
            levellen =  len(q)

            if forward:
                result.append(level)
            else:
                result.append(level[::-1])
            forward = not forward

        return result



