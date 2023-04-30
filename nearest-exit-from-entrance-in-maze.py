class Solution:
    def bfs(self,maze,entrance):
        ans = 0
        a,b = entrance
        queue = deque([(a,b)])
        visited = set((a,b))

        def inbound(i,j):
            return 0 <= i < len(maze) and 0 <= j < len(maze[0])

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while queue:
            n = len(queue)
            for _ in range(n):
                i,j = queue.popleft()
                if i == 0 or i == len(maze)-1 or j == 0 or j == len(maze[0])-1:
                    if [i,j] != entrance:
                        return ans
        
                for tx,ty in directions:
                    row = i + tx
                    col = j + ty

                    if inbound(row,col) and maze[row][col] == "." and (row,col) not in visited:
                        queue.append((row,col))
                        visited.add((row,col))
            ans += 1
        return -1
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        return self.bfs(maze,entrance)