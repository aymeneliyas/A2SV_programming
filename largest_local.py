class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        rowlen = len(grid)
        collen = len(grid[0])
        for row in range(rowlen-2):
            temparr = []
            for col in range(collen-2):
                temp = []
                temp.append(max(grid[row][col:col+3]))
                temp.append(max(grid[row+1][col:col+3]))
                temp.append(max(grid[row+2][col:col+3]))
                temparr.append(max(temp))
            ans.append(temparr)               
        return ans
