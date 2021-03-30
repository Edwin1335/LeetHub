#   nums = [5,7,7,8,8,10]    target = 8
#
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        min_index = -1
        max_index = -1
        found = False
        
        for index, val in enumerate(nums):
            if val == target and not found:
                min_index = index
                max_index = index
                found = True
            elif val == target and found:
                max_index = index
                
        return [min_index, max_index]