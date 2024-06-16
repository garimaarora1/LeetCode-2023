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
        emp_map = {emp.id: emp for emp in employees}
        
        total_importance = 0 
        
        queue = deque()
        queue.append(id)
        
        while queue:
            emp_id = queue.popleft()
            emp = emp_map[emp_id]
            total_importance += emp.importance
            for subordinate in emp.subordinates:
                queue.append(subordinate)

        return total_importance