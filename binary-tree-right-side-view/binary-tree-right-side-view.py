# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return
			
        ans = []
        q = [root]
        subq = []
        
        while q:
            element = q.pop(0)
            
            if element.left:
                subq.append(element.left)
            if element.right:
                subq.append(element.right)
            
            if not q:
                ans.append(element.val)
                q = subq
                subq = []
                
        return ans