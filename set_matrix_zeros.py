class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        points = []
        rowlen = len(matrix)
        collen = len(matrix[0])
        for row in range(rowlen):
            for col in range(collen):
                if matrix[row][col] == 0:
                    points.append([row,col])
        print(points)
        for point in points:
            
            for i in range(collen):
                matrix[point[0]][i] = 0
            for j in range(rowlen):
                matrix[j][point[1]] = 0
