# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        # Base Case
        if not head:
            return None
        if not head.next:
            return head
        
        # Get size of list      Time: O(n/2)-> O(n)
        counter = 1
        current = head.next
        counter += 1
        while current and current.next:
            counter += 2
            current = current.next.next
        if not current:
            counter -=1
            
        # Begin Rotating        Time: O(n)
        k = k % counter
        print(k, counter)
        if k == 0:
            return head
        
        current = head
        start = head
        back = None
        counter = 1
        # None  1-> 2-> 3-> 4-> 5
        #                       C
        #                   S
        #               B
        while current.next:
            if counter >= k:
                back = start
                start = start.next
            current = current.next
            counter += 1
        back.next = None
        current.next = head
        head = start
        return head
    

            
        
        
                