# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        graph = defaultdict(TreeNode)
        visited = set()
        for p, c, left in descriptions:
            if p not in graph:
                graph[p] = TreeNode(p)
            if c not in graph:
                graph[c] = TreeNode(c)
            if left:
                graph[p].left = graph[c]
            else:
                graph[p].right = graph[c]
            visited.add(c)

        for v, node in graph.items():
            if v not in visited:
                return node