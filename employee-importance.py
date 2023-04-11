"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def __init__(self):
        self.ans = 0

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        visited = set()
        def dfs(node,visited):
            visited.add(node)
            self.ans += node.importance
            for sub in node.subordinates:
                for emp in employees:
                    if emp.id == sub:
                        dfs(emp,visited)
            
            
        for employe in employees:
            if employe.id == id:
                print(employe.id)
                dfs(employe,visited)
        
        return self.ans