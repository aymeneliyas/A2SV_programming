class Solution:
    def knightDialer(self, n: int) -> int:

        directions=[(2,-1),(2,1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        mod = (10**9) + 7
        def inbound(row,col):
            return ((0<=row<3) and (0<=col<3)) or (row==3 and col==1)
        
        @cache
        def getPath(n,i,j):
            
            if n == 0:
                return 1
            
            total = 0
            for x,y in directions:
                r = i + x
                c = j + y
                if inbound(r,c):
                    total += getPath(n-1,r,c) % mod
            
            return total
        
        total = 0
        for i in range(4):
            for j in range(3):
                if (i,j) == (3,0) or (i,j) == (3,2):
                    continue
                total += getPath(n-1,i,j)
       
        return total % mod