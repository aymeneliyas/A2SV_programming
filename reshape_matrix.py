class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        tmp = []
        output = []
        rowlen = len(mat)
        collen = len(mat[0])
        if r*c != rowlen*collen:
            return mat
        for row in range(rowlen):
            for col in range(collen):
                tmp.append(mat[row][col])
        
        ptr = 0
        for row in range(r):
            out = []
            for col in range(c):
                out.append(tmp[ptr])
                ptr += 1
            output.append(out)
        return output
