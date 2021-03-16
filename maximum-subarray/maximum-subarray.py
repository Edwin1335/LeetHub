# -2 -3 -4 -5 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for x in range(1, len(nums)):
            if nums[x-1] > 0:
                nums[x] += nums[x-1]
        return max(nums)