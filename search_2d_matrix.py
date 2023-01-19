class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        target_row = []
        for row in range(len(matrix)):
            if target > matrix[row][len(matrix[0])-1]:
                continue
            else:
                target_row = matrix[row]
                break
        if target in target_row:
            return True
        return False
