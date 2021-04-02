class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.__head = Node("Dummy", "Least")
        self.__tail = Node("Dummy", "Most")
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__cache = {}
        self.__size = 0
        
    def get(self, key: int) -> int:
        get_val = -1
        if key in self.__cache:
            get_val = self.__cache[key].val
            self.__remove(self.__cache[key])
            self.__append(self.__cache[key])  
        return get_val

    def put(self, key: int, value: int) -> None:
        if key in self.__cache:
            print("Found")
            self.__remove(self.__cache[key])
            
        self.__cache[key] = Node(key, value)
        self.__append(self.__cache[key])
        
        if self.__size > self.capacity:
            toRemove = self.__tail.prev
            self.__remove(toRemove)
            del self.__cache[toRemove.key]
            
    def __append(self, node):
        node.next = self.__head.next
        node.prev = self.__head
        self.__head.next.prev = node
        self.__head.next = node
        self.__size += 1
    
    def __remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.__size -= 1
    
    def __str__(self):
        out = "Least-> "
        cur = self.__head.next
        while cur != self.__tail:
            out += f" <-{cur.val}-> "
            cur = cur.next
        out += " <-Most"
        return out
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)