class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = defaultdict(int)
        self.lru = []

    def get(self, key: int) -> int:
        # print(self.dic)
        idx = 0
        if key in self.dic:
            self.lru.remove(key)
            self.lru.insert(0,key)
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # print(self.capacity,len(self.lru))
        # print(self.dic,self.lru)
        if key in self.dic:
            self.dic[key] = value
            self.lru.remove(key)
            self.lru.insert(0,key)
            return 
        elif len(self.dic) == self.capacity:
            val = self.lru.pop()
            del self.dic[val]
            self.dic[key] =value
            self.lru.insert(0,key)
        else:
            self.dic[key] = value
            self.lru.insert(0,key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)