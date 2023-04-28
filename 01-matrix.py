class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        queue = deque()
        visited = set()

        def inbound(i,j):
            return 0<=i<len(mat) and 0<= j < len(mat[0])
    
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            length = len(queue)
            for _ in range(length):
                i, j = queue.popleft()
                mat[i][j] = ans

                for tx, ty in directions:
                    row = i + tx
                    col = j + ty

                    if inbound(row, col) and (row, col) not in visited and mat[row][col] == 1:
                        queue.append((row, col))
                        visited.add((row, col))

            ans += 1

        
        return mat