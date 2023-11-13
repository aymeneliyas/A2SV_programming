class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        i, j = 0, 0
        def inbound(i, j): 
            return 0 <= i < len(mat) and 0 <= j < len(mat[0])

        while inbound(i, j):
            ans += mat[i][j]
            mat[i][j] = 0
            i += 1
            j += 1
        
        i, j = len(mat) - 1, 0
        
        while inbound(i, j):
            ans += mat[i][j]
            i -= 1
            j += 1

        return ans