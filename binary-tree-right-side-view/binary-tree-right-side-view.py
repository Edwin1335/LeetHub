# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return
        ans = []
        q = deque()
        q.append(root)
        
        while len(q) > 0:
            temp_queue = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    temp_queue.append(node.left)
                if node.right:
                    temp_queue.append(node.right)
                if i ==  size-1:
                    ans.append(node.val)
            q += temp_queue
            
        return ans