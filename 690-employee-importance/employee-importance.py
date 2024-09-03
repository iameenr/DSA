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

        total_importance = 0
        q = deque([id])
        while q:
            # node = q.popleft()
            e = empd[q.popleft()]
            total_importance += e.importance

            for nei in e.subordinates:
                q.append(nei)

        return total_importance

    