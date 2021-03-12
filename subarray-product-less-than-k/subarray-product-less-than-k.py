# [10, 5, 2, 6]
#
# prod_count = 8
# Product = 60
#
# S   i
#   [1, 1, 1, 1]
# 

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or k == 0:
            return 0

        prod_count = 0
        product = 1
        start = -1
        
        for i in range(len(nums)):
            product = product * nums[i]
            while product >= k and start < i:
                start += 1
                product = product / nums[start]
            if product < k:
                prod_count += i - start
            
        return prod_count