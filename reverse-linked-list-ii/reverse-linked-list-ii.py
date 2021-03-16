# p = 2 -> None
# c = 3
# nxt = 4
#
# 2-> 3-> 4-> 5
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        current = head
        prev = None
        counter = 1
        while counter < left:
            prev = current
            current = current.next
            counter += 1
        if prev:
            prev.next = self.reverseLink(current, (right - left))
        else:
            head = self.reverseLink(current, (right - left))
        return head
    
    def reverseLink(self, head, count):
        current = head
        prev = None
        counter = -1
        nxt = None
        print(f"Loc: {current.val}")
        while current and counter < count:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            counter += 1
        if nxt:
            head.next = nxt
        return prev
        
        