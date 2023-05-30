class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def inbound(row,col):
            return 0 <= row < m and 0 <= col < n
        
        direction = [(1,0),(0,1)]
        def solve(row,col,dic):
            if row == m-1 and col == n-1:
                return 1
            
            if (row,col) in dic:
                return dic[(row,col)]
            tot = 0
            for r,c in direction:
                newrow = r + row
                newcol = c + col

                if inbound(newrow,newcol):
                    val = solve(newrow,newcol,dic)
                    tot += val     
                
            dic[(row,col)] = tot
            return tot
        
        res = solve(0,0,{})
        return res