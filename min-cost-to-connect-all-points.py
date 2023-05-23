class unionFind:
    def __init__(self,n):
        self.rep = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}
    
    def find(self,x):
        if self.rep[x] == x:
            return x
        
        val = self.find(self.rep[x])
        return val
    
    def union(self,x,y):
        repx =  self.find(x)
        repy = self.find(y)

        sizex = self.size[repx]
        sizey = self.size[repy]

        if sizex > sizey:
            self.rep[repy] = repx
            self.size[repx] += self.size[repy]
        else:
            self.rep[repx] = repy
            self.size[repy] += self.size[repx]
        

    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        un = unionFind(len(points))
        size = len(points)
        arr = []
        for i in range(size):
            for j in range(size):
                if i == j:
                    continue
                x1,y1 = points[i]
                x2,y2 = points[j]

                val = abs(x2-x1) + abs(y2-y1)
                arr.append((i,j,val))
        ans = 0
        arr.sort(key=lambda i:i[2])
        for i,j,val in arr:
            if un.find(i) != un.find(j):
                ans += val
                un.union(i,j)
        
        return ans