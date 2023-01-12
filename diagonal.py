from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_len = len(mat)
        col_len = len(mat[0])
        dic = defaultdict(list)

        for row in range(row_len):
            for col in range(col_len):
                dic[row+col].append(mat[row][col])
        
        
        ans = []
        for index,val in enumerate(dic.values()):
            
            if index % 2 != 0:
                ans += val
            else:
                ans += val[::-1]
        
        return ans
