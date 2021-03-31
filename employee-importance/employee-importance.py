"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
# [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
# 
# dfs()
    

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return 0
        
        emp = {e.id : e for e in employees}
        
        def dfs(list_empl):
            if not list_empl:
                return 0
            total = 0
            for e in list_empl:
                total += emp[e].importance + dfs(emp[e].subordinates)
                
            return total
                
        
        return emp[id].importance + dfs(emp[id].subordinates)
        
        
            
            