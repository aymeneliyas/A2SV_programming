class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        visited = set()
        
        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def dfs(i,j,depth):
            visited.add((i,j))
            if not inbound(i,j) or grid[i][j] == 0:
                return 0
            total = 0
            for tx,ty in directions:
                x = i + tx
                y = j + ty

                if inbound(x,y) and (x,y) not in visited:
                    total += dfs(x,y,depth+1)
                
            return total + 1
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area, dfs(i,j,0))
        return area