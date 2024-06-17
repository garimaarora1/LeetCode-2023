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
        emp_map = {employee.id: employee for employee in employees}
        queue = deque()
        queue.append(id)
        total_importance = 0
        while queue:
            curr_id = queue.popleft()
            employee = emp_map[curr_id]
            total_importance += employee.importance
            for subordinate in employee.subordinates:
                queue.append(subordinate)
        return total_importance