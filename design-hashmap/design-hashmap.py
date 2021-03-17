class Node:
    def __init__(self, key=-1, val=-1, next = None):
        self.key = key
        self.val = val
        self.next = next
        
class MyHashMap:

    def __init__(self):
        self.table = [Node("Dummy") for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        hsh = self.hash(key)
        current = self.table[hsh]
        while current.next:
            if current.next.key == key:
                current.next.val = value
                return
            current = current.next
        
        newNode = Node(key, value)
        current.next = newNode

    def get(self, key: int) -> int:
        hsh = self.hash(key)
        current = self.table[hsh].next
        while current:
            if current.key == key:
                return current.val
            current = current.next
        return -1
        

    def remove(self, key: int) -> None:
        hsh = self.hash(key)
        prev = self.table[hsh]
        current = self.table[hsh].next
        while current:
            if current.key == key:
                prev.next = current.next
                current.next = None
                del current.val
                del current.key
                return
            prev = current
            current = current.next
        
    def hash(self, key):
        return key % len(self.table)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)