

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        lenarr = len(arr)
        visited = set()
        q = deque([start])
        while q:
            index = q.popleft()
            visited.add(index) 
            nodeval = arr[index]
            if nodeval == 0:
                return True

            neigh = index - nodeval
            if neigh >= 0 and neigh not in visited:
                q.append(neigh)
                
            neigh = index + nodeval
            if neigh < lenarr and neigh not in visited:
                q.append(neigh)

            
        return False

