# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:        
        if not root:
            return None
        
        out = []
        q = deque()
        q.append(root)
        
        while q:
            to_append = list()
            for _ in range(len(q)):
                popped = q.popleft()
                to_append.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            out.append(to_append)
        return out