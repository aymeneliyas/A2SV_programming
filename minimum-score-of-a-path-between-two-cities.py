class unionFind:
    def __init__(self,n):
        self.rep = {i:i for i in range(n+1)}
        self.size = {i:1 for i in range(n+1)}

    def find(self,x):
        if self.rep[x] == x:
            return x
        val = self.find(self.rep[x])
        self.rep[x] = val
        return val

    def union(self,x,y):
        rep_x = self.find(x)
        rep_y = self.find(y)

        if rep_x == rep_y:
            return

        size_x = self.size[rep_x]
        size_y = self.size[rep_y]

        if size_x > size_y:
            self.rep[rep_y] = rep_x
            self.size[rep_x] += size_y
        else:
            self.rep[rep_x] = rep_y
            self.size[rep_y] += size_x        

    def connected(self,x,y):
        x = self.find(x)
        y = self.find(y)
        
        return x == y

    
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = unionFind(n)
        roadcost = defaultdict(lambda:float('inf'))
        for start,end,distance in roads:
            repstart = uf.find(start)
            repend = uf.find(end)
            val = min(roadcost[repstart],roadcost[repend],distance)
            
            uf.union(repstart,repend)
            roadcost[uf.find(repstart)] = val
        return roadcost[uf.find(1)]