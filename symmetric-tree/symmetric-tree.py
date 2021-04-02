# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.mirror(root.left, root.right)
    
    def mirror(self, left, right):
        if not left or not right:
            return left == right
        
        val_same = left.val == right.val
        left_symmetric = self.mirror(left.left, right.right)
        right_symmetric = self.mirror(left.right, right.left)
        
        return val_same and left_symmetric and right_symmetric