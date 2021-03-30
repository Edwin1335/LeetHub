
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mydic = {}
        out = 0
        for x in nums:
            mydic[x] = mydic.get(x, 0) + 1
        
        for x in mydic:
            if mydic[x] == 1:
                out += x
        
        return out