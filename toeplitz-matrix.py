class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        dic = defaultdict(list)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                dic[row-col].append(matrix[row][col])
        
        for key in dic.keys():
            for val in range(len(dic[key])-1):
                if dic[key][val] != dic[key][val+1]:
                    return False
        return True
