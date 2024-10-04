from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        

        seen = {}

        def dfs(node, copynode):
            seen[node] = copynode
            copynode.val = node.val 
            
            
            for nei in node.neighbors:
                if nei not in seen:  
                    new_clone = Node() 
                    copynode.neighbors.append(new_clone)  
                    dfs(nei, new_clone)  
                else:
                    copynode.neighbors.append(seen[nei])
        
    
        copyheadnode = Node()  
        dfs(node, copyheadnode)  
        
        return copyheadnode
