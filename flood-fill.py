class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        visited = set()
        def inbound(i,j):
            return 0 <= i < len(image) and 0 <= j < len(image[0])
        
        val = image[sr][sc]

        def dfs(i,j):
            visited.add((i,j))
            for tx,ty in directions:
                x = i + tx
                y = j + ty
                
                if inbound(x,y) and (x,y) not in visited and image[x][y] == val:
                    image[x][y] = color
                    dfs(x,y)

        image[sr][sc] = color
        dfs(sr,sc)
        return image