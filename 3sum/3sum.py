class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        triple = {}
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums)-1:
            left = i + 1
            right = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            if nums[i] + nums[left] + nums[right] > 0:
                nums = nums[:right]
            elif nums[i] + nums[right-1] + nums[right] < 0:
                nums = nums[left:]
                i = 0
            else:
                while left < right:
                    if nums[i] + nums[left] + nums[right] < 0:
                        left += 1
                    elif nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        triple[nums[i], nums[left], nums[right]
                               ] = [nums[i], nums[left], nums[right]]
                        right -= 1
                        left = i + 1
                i += 1
        
        return map(list, triple)

        