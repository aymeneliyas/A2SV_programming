class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island1 = deque()
        q = deque()
        visited = set()
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        def inbound(x,y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island1.append((i,j))
                    q.append((i,j))
                    visited.add((i,j))
                    break
            if len(island1) == 1:
                break
        while q:
            n = len(q)
            for _ in range(n):
                i,j = q.popleft()
                for tx,ty in directions:
                    x =  i + tx
                    y = j + ty

                    if inbound(x,y) and (x,y) not in visited and grid[x][y] == 1:
                        q.append((x,y))
                        visited.add((x,y))
                        island1.append((x,y))

        count = 0
        while island1:
            n = len(island1)
            for _ in range(n):
                i,j = island1.popleft()
                for tx,ty in directions:
                    x = tx + i
                    y = ty + j

                    if inbound(x,y) and (x,y) not in visited:
                        if grid[x][y] == 1:
                            return count
                        island1.append((x,y))
                        visited.add((x,y))
            count += 1