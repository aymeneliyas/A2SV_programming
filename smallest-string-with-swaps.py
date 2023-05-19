class unionFind:
    def __init__(self,n):
        self.rep = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}

    def find(self,x):
        if self.rep[x] == x:
            return x
        val = self.find(self.rep[x])
        self.rep[x] = val
        return val

    def union(self,x,y):
        rep_x = self.find(x)
        rep_y = self.find(y)

        self.rep[rep_x] = rep_y       

    def connected(self,x,y):
        x = self.find(x)
        y = self.find(y)
        
        return x == y
        


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        size = len(s)
        un = unionFind(size)

        for x,y in pairs:
            un.union(x,y)
        
        dic = defaultdict(list)
        for key,val in un.rep.items():
            heappush(dic[un.find(val)],s[key])
        
        arr = []
        for i in range(size):
            val = un.find(i)
            a = heappop(dic[val])
            arr.append(a)
        
        return "".join(arr)