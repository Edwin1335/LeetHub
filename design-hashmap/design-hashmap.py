class Node:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next
        
    def getKey(self):
        return self.key
    
class Linked:
    def __init__(self):
        self.Head = Node("Dummy")
    
    def insert(self, key, val):
        newNode = Node(key, val)
        current = self.Head
        while current.next:
            if current.next.key == key:
                current.next.val = val
                return
            current = current.next;
        current.next = newNode
        
    def retrieve(self, key):
        current = self.Head.next
        while current:        
            if current.key == key:
                return current.val
            current = current.next;
        return -1
    
    def remove(self, key):
        prev = self.Head
        current = self.Head.next
        while current and current.key != key:
            prev = current
            current = current.next;
        if current:
            prev.next = current.next
            current.next = None
            del current.val
            del current.key
    
    def __str__(self):
        out = ""
        cu = self.Head.next
        while cu:
            out += f"{cu.key}:{cu.val}-> "
            cu = cu.next
        return out
        
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 0xff
        self.maps = [[] for _ in range(self.buckets+1)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key & self.buckets 
        
        for i, val in enumerate(self.maps[index]):
            if val[0] == key:
                self.maps[index][i][1] = value
                return
            
        self.maps[index].append([key, value])  

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key & self.buckets 
        
        for val in self.maps[index]:
            if val[0] == key: return val[1]
            
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key & self.buckets 
        bucket = self.maps[index]
        
        for i, val in enumerate(bucket):
            if val[0] == key:
                if i < len(bucket)-1: bucket[i] = bucket[-1]
                bucket.pop()
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)