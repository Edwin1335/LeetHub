# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        before = None
        prev = head
        current = head.next        
        #  1->2->3-> 4-> 5->None
        #
        # C = 2
        # B -> 1 -> None
        # prev(2)-> None
        #
        while current:
            prev.next = before
            before = prev
            prev = current
            current = current.next
        prev.next = before
        return prev