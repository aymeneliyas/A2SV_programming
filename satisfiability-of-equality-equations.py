class unionFind:
    def __init__(self):
        self.rep = {chr(ord('a')+i) : chr(ord('a')+i) for i in range(27)}
        self.size = {chr(ord('a')+i):1 for i in range(27)}

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
    def equationsPossible(self, equations: List[str]) -> bool:
        char = set()
        edges = []
        un = unionFind()
        for word in equations:
            if word[1] == "=":
                un.union(word[0],word[3])
        for word in equations:
            if word[1] == "!":
                if un.find(word[0]) == un.find(word[3]):
                    return False
        return True