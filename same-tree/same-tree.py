# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.rec_check_same(p, q)
        
    def rec_check_same(self, p, q):
        if p != None and q != None:
            if p.val != q.val:
                return False
            else:
                return self.rec_check_same(p.left, q.left) and self.rec_check_same(p.right, q.right)
        elif p != None and q == None:
            return False
        elif p == None and q != None:
            return False
        
        return True

        