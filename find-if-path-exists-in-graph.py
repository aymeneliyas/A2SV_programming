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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        un = unionFind(n)
        for x,y in edges:
            un.union(x,y)

        return un.connected(source,destination)