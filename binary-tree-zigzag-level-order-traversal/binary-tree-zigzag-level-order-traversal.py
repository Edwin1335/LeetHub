# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: 
            return []
        q = deque()
        q.appendleft(root)
        out = []
        flag = True
        while q:
            new_list = []
            for _ in range(len(q)):
                node = q.popleft()
                new_list.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(new_list if flag else new_list[::-1])
            flag = False if flag else True
            
        return out
        