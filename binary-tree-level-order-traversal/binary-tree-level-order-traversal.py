# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        arr = []
        self.__levelRec(root, arr, 0)
        return arr

    def __levelRec(self, root, arr: list(), height: int()) -> list():
        if not root:
            return
        if height >= len(arr):
            newarr = []
            arr.append(newarr)
        arr[height].append(root.val)
        self.__levelRec(root.left, arr, height+1)
        self.__levelRec(root.right, arr, height+1)
        
        