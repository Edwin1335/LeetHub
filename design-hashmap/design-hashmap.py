class MyHashMap:

    def __init__(self):
        self.hash = [-1]*100000
        

    def put(self, key: int, value: int) -> None:
        self.hash[self.getHash(key)] = value
        
    def get(self, key: int) -> int:
        return self.hash[self.getHash(key)]
        

    def remove(self, key: int) -> None:
        self.hash[self.getHash(key)] = -1
    
    def getHash(self, val):
        return val % 100000
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)