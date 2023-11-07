class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] > target:
                return False
            
            index = bisect_left(row,target)
            if index < len(matrix[0]) and row[index] == target:
                return True
        
        return False