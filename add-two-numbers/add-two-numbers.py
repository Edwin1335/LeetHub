# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        newList = ListNode("Dummy")
        head = newList
        current1 = l1
        current2 = l2
        carry = 0
        
        while current1 and current2:
            addition = current1.val + current2.val + carry
            if addition >= 10:
                carry = 1
            else:
                carry = 0
            newNode = ListNode(addition % 10)
            head.next = newNode
            head= head.next
            current1 = current1.next
            current2 = current2.next
        
        while current1:
            addition = current1.val + carry
            if addition >= 10:
                carry = 1
            else:
                carry = 0
            newNode = ListNode(addition % 10)
            head.next = newNode
            head= head.next
            current1 = current1.next
        while current2:
            addition = current2.val + carry
            if addition >= 10:
                carry = 1
            else:
                carry = 0
            newNode = ListNode(addition % 10)
            head.next = newNode
            head= head.next
            current2 = current2.next
            
        if carry == 1:
            newNode = ListNode(1)
            head.next = newNode
            head    = head.next
        return newList.next

            
            