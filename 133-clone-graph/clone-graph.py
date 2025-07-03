"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        def dfs(node, clone_node):
            clone_node.val = node.val
            cloned[node] = clone_node

            for neighbor in node.neighbors:
                if neighbor not in cloned:
                    clone_neighbor = Node()
                    dfs(neighbor, clone_neighbor)
                    clone_node.neighbors.append(clone_neighbor)
                else:
                    clone_node.neighbors.append(cloned[neighbor])


        cloned = {} # node : clone_node
        clone_head = Node()
        dfs(node, clone_head)
        return clone_head

