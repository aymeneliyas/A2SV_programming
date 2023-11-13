class Solution:
    def __init__(self):
        self.count = 0

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        count = 0

        def outBound(i,j):
            return (0 <= i < len(grid) and 0 <= j < len(grid[0]))
        
        def dfs(i,j):
            visited.add((i,j))
            for dx,dy in directions:
                x = i + dx
                y = j + dy
                if not outBound(x,y):
                    self.count += 1
                elif grid[x][y] == 0:
                    self.count += 1
                elif (x,y) not in visited:
                    dfs(x,y)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return self.count
        
                    
        