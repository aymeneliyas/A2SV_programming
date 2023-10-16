class RandomizedSet:

    def __init__(self):
        self.arr = []        
        self.dic = defaultdict()

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.arr.append(val)
            self.dic[val] = len(self.arr)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        # print(dic,val)
        if val in self.dic:
            idx = self.dic[val]
            last = self.arr[-1]
            self.arr[self.dic[val]],self.arr[-1] = self.arr[-1],self.arr[self.dic[val]]    
            self.arr.pop()
            self.dic[last] = idx
            del self.dic[val]    
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()