# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        list_dic = dict()
        travA = headA
        travB = headB
        while travA != None or travB != None:
            if id(travA) in list_dic:
                return list_dic[id(travA)]
            elif travA != None: 
                list_dic[id(travA)] = travA
                travA = travA.next
            if id(travB) in list_dic:
                return list_dic[id(travB)]
            elif travB != None:
                list_dic[id(travB)] = travB
                travB = travB.next
                
        return None
        