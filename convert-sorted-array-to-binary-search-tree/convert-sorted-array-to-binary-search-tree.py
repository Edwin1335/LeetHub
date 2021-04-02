# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        middle = len(nums) // 2
        newNode = TreeNode(nums[middle], self.sortedArrayToBST(nums[:middle]), self.sortedArrayToBST(nums[middle + 1:]))        
        return newNode

