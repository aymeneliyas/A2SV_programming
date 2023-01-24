class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(9):
            rowseen = []
            colseen = []
            for col in range(9):
                if board[col][row] in colseen:
                    return False
                elif board[col][row] != ".":  
                    colseen.append(board[col][row])
                    
            for col in range(9):
                if board[row][col] in rowseen :
                    return False
                elif board[row][col] != ".":
                    rowseen.append(board[row][col])
        
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = []
                for i in range(3):
                    for j in range(3):
        
                        if board[row+i][col+j] in seen:
                            return False
                        else:
                            if board[row+i][col+j] != ".":
                                seen.append(board[row+i][col+j])
                        
                
        return True
