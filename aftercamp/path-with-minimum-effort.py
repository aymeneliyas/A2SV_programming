class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = [(0,0,0)]
        ans = 0
        def inbound(i,j):
            return 0 <= i < len(heights) and 0 <= j < len(heights[0])
        visited = set()
        while queue:
            minpath,i,j =heapq.heappop(queue)
            ans = max(ans,minpath)
            if i == len(heights)-1 and j == len(heights[0])-1:
                return ans

            visited.add((i,j)) 

            for tx,ty in directions:
                nx = i + tx
                ny = j + ty

                if inbound(nx,ny) and (nx,ny) not in visited:
                    path = abs(heights[i][j] - heights[nx][ny])
                    heapq.heappush(queue,(path,nx,ny))
            
        return ans