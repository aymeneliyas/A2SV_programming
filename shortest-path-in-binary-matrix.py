class Solution:
    def bfs(self,grid):
        ans = 1
        queue = deque([(0,0)])
        # queue.append((0,0))
        visited = set([(0,0)])
        directions = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0])-1]:
            return -1
        if len(grid) == 1:
            return 1
        while queue:
            n = len(queue)
            ans += 1
            for _ in range(n):
                i,j = queue.popleft()
                for tx,ty in directions:
                    x = i + tx
                    y = j + ty

                    if x == len(grid)-1 and y == len(grid[0])-1:
                        return ans
            
                    if inbound(x,y) and (x,y) not in visited and grid[x][y] == 0:
                        queue.append((x,y))
                        visited.add((x,y))
                    
        return -1
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)