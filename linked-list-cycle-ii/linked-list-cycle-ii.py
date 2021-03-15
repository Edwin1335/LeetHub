# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        repeated = dict()
        current = head
        while current:
            if current in repeated:
                return repeated[current]
            repeated[current] = current
            current = current.next
        
        return None
        