class unionFind:
    def __init__(self,n):
        self.rep = {chr(ord('a')+i) : chr(ord('a')+i) for i in range(27)}
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

        if rep_x < rep_y:
            self.rep[rep_y] = rep_x
        else:
            self.rep[rep_x] = rep_y      

    def connected(self,x,y):
        x = self.find(x)
        y = self.find(y)
        
        return x == y

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        un = unionFind(len(s1))
        
        for i in range(len(s1)):
            un.union(s1[i],s2[i])
        
        answer = ""
        for i in baseStr:
            answer += un.find(i)
        return answer