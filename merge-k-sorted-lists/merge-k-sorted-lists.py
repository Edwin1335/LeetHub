# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        q = PriorityQueue(maxsize=k)
        dummy = ListNode()
        current = dummy
        
        # Insert heads into queue
        for index, node in enumerate(lists):
            if node:
                q.put((node.val, index, node))
        while not q.empty():
            popped = q.get()
            current.next, index = popped[2], popped[1]
            current = current.next
            if current.next:
                q.put((current.next.val, index, current.next))
                
        return dummy.next

    

# Queue:
#                   C
# dummy-> 1 -> 1 -> 2-> 6 
#     
# 
# 3-> 4
# 4 -> 5    
