class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupl = dict()
        for x in nums:
            if x in dupl:
                return True
            dupl[x] = x
        return False