from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dict = defaultdict(int)
        row_len = len(grid)
        col_len = len(grid[0])
        
        for i in range(row_len):
            nums = ""
            for j in range(col_len):
                nums += str(grid[i][j])
                nums += "#"
            
            row_dict[nums] += 1
        
        ans = 0
        for i in range(row_len):
            nums = ""
            for j in range(col_len):
                nums += str(grid[j][i])
                nums += "#"
            ans += row_dict[nums]
        return ans
