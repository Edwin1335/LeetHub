from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        ret = []
        path = ""
        index = 0
        self.DFS(digits, phone, "", ret,  0)
        
        return ret
        
    def DFS(self, digits, phone, path, ret, index):
        if index >= len(digits):
            ret.append(path)
            return 
        
        for c in phone[digits[index]]:
            self.DFS(digits, phone, path + c, ret, index+1)