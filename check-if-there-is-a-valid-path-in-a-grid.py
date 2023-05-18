class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
      rep = {}
      size = {}
      rows = len(grid)
      cols = len(grid[0])
      for row in range(len(grid)):
        for col in range(len(grid[0])):
          rep[(row,col)] = (row,col)
          size[(row,col)] = 1

      def find(x,rep):
        if rep[x] == x:
            return x
        rep[x] = find(rep[x],rep)
    
        return rep[x]

      def union(x,y,rep):
          rep_x = find(x,rep)
          rep_y = find(y,rep)

          if rep_x == rep_y:
              return

          size_x = size[rep_x]
          size_y = size[rep_y]

          if size_x > size_y:
              rep[rep_y] = rep_x
              size[rep_x] += size_y
          else:
              rep[rep_x] = rep_y
              size[rep_y] += size_x        

      def connected(x,y,rep):
          x = find(x,rep)
          y = find(y,rep)
          
          return x == y
      
      def inbound(row,col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) 

      def check(row,col):
        neighbors = {
                  1: [(0, -1, {1, 4, 6}), (0, 1, {1, 3, 5})],
                  2: [(-1, 0, {2, 5, 6}), (1, 0, {2, 3, 4})],
                  3: [(0, -1, {1, 4, 6}), (1, 0, {2, 5, 6})],
                  4: [(1, 0, {2, 5, 6}), (1, 0, {2, 3, 4})],
                  5: [(-1, 0, {2, 3, 4}), (0, -1, {1, 4, 6})],
                  6: [(-1, 0, {2, 3, 4}), (0, 1, {1, 3, 5})]
              }
        for tx,ty,streets in neighbors[grid[row][col]]:
          newrow = row + tx
          newcol = col + ty

          if inbound(newrow,newcol) and grid[newrow][newcol] in streets:
            union((row,col),(newrow,newcol),rep)

      for row in range(len(grid)):
        for col in range(len(grid[0])):
          check(row,col)

      return connected((0, 0), (rows - 1, cols - 1),rep)