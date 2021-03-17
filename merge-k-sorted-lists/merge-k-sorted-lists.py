# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 
#   PQ  [()(C2, 1)(C1, 2)]
#   retriveNode = PQ.get()-> C3
#   [C2]->(1)->(2)->(4)
#   [C1]->(2)->(6)
#   [C3]->(4)->(5)
                     
#   [Trav]->[C3]->(1)->(4)->(5)
#   Head("Dummy")->
#   Trav = Head
#   Trav.next = retriveNode
#   

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        que = PriorityQueue()
        sorted_list = ListNode("Dummy")
        trav = sorted_list
        
        # Insert into queue in ascending order Time: O(nLogn)
        for index, lst in enumerate(lists):
            if lst:
                que.put((lst.val, index, lst))

        # Loop until queue is empty Time: O(n)
        while not que.empty():
            q_value = que.get()
            index, temp = q_value[1], q_value[2]
            trav.next = temp
            trav = trav.next
            if trav.next:
                que.put((trav.next.val, index, trav.next))
            
        # Return sorted list
        return sorted_list.next
        
        
            
        
        