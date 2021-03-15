"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        mydic = {None: None}
        current = head
        while current:
            mydic[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            mydic[current].next = mydic[current.next]
            mydic[current].random = mydic[current.random]
            current = current.next
        
        return mydic[head]
        