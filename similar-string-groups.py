class union:
    def __init__(self,n):
        self.rep = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
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
    def numSimilarGroups(self, strs: List[str]) -> int:
        un = union(len(strs))

        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                count = 0
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        count += 1

                if count < 3:
                    un.union(i,j)
        
        ans = set()
        for i in range(len(strs)):
            ans.add(un.find(i))
        return len(ans)