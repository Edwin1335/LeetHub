# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        tree = self.rec(nums)
        return tree
    
    def rec(self, nums):
        if not nums:
            return
        middle = len(nums) // 2
        newNode = TreeNode(nums[middle], self.rec(nums[:middle]), self.rec(nums[middle + 1:]))
        return newNode
