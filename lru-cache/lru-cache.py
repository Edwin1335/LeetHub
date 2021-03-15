class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node.
        
class LRUCache:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__least = Node("Dummy", "Least")
        self.__most = Node("Dummy", "Most")
        self.__least.next = self.__most
        self.__most.prev = self.__least
        self.__cache = dict()
        

    def get(self, key: int) -> int:
        toReturn = -1
        if key in self.__cache and self.__cache[key].next != self.__most:
            toReturn = self.__cache[key].value
            self.__delete(self.__cache[key])
            self.__insert(self.__cache[key])
        elif key in self.__cache and self.__cache[key].next == self.__most:
            toReturn = self.__cache[key].value
        return toReturn 
        

    def put(self, key: int, value: int) -> None:
        if key in self.__cache:
            self.__delete(self.__cache[key])

        self.__cache[key] = Node(key, value)
        self.__insert(self.__cache[key])

        if len(self.__cache) > self.__capacity:
            delete = self.__least.next
            self.__delete(delete)
            del self.__cache[delete.key]
            
            
    def __delete(self, node:Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def __insert(self, node:Node):
        node.prev = self.__most.prev
        node.next = self.__most
        self.__most.prev.next = node
        self.__most.prev = node

    def __str__(self):
        out = "Least-> "
        cur = self.__least.next
        while cur != self.__most:
            out += f" <-{cur.value}-> "
            cur = cur.next
        out += " <-Most"
        return out
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)