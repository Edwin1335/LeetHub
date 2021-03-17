#               2, 3, 6, 7,     Target=7
#   Path[2]  ->   2(T=6)->    4(T=) 
#   Path[2,3]->
#   Path[]
#   Path[]
#   Path[]
#   Path[]
#   Path[]
#

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        self.combination(candidates, target, [], out)
        return out
    def combination(self, candidates, target, path, out):
        if target < 0:
            return
        if target == 0:
            out.append(path)
            return
        for i in range(len(candidates)):
            self.combination(candidates[i:], target-candidates[i], path+[candidates[i]], out)
            
        
        