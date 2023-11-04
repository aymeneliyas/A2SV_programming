class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            rowseen = set()
            colseen = set()
            for j in range(len(board[0])):
                if board[i][j] in rowseen:
                    return False
                
                if board[i][j] != ".":
                    rowseen.add(board[i][j])
            
            for j in range(len(board[0])):
                if board[j][i] in colseen:
                    return False
                if board[j][i] != ".":
                    colseen.add(board[j][i])

        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        if board[row+i][col+j] in seen:
                            return False
                        if board[row+i][col+j] != ".":
                            seen.add(board[row+i][col+j])
        
        return True