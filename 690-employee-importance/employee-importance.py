"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        empd = {} # 1 : Employee() 
        for e in employees:
            empd[e.id] = e

        def bfs(start):
            summ = 0
            q = deque([start])
            while q:
                node = q.popleft()
                e = empd[node]
                summ += e.importance

                for nei in e.subordinates:
                    q.append(nei)

            return summ

        return bfs(id)
    