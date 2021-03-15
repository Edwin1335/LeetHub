class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        n = len(nums)
        curr_sum = 0
        min_len = n + 1
        start = 0
        end = 0
        while (end < n):
            while (curr_sum < target and end < n):
                curr_sum += nums[end]
                end += 1

            while (curr_sum >= target and start < n):

                if (end - start < min_len):
                    min_len = min(min_len,(end - start))

                curr_sum -= nums[start]
                start += 1

        return min_len
                