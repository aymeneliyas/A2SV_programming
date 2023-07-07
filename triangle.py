class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        size = len(triangle)
        length = list(map(lambda x: len(x), triangle))
        memo = {}

        def dp(row, col):
            if row >= size or col >= length[row]:
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            memo[(row,col)] = min(dp(row + 1, col), dp(row + 1, col + 1)) + triangle[row][col]
            return memo[(row, col)]
        return dp(0,0)