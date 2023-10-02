class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        dp = {}
        def dfs(i,j):
            if i == len(satisfaction):
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            pick = satisfaction[i] * j + dfs(i+1,j+1)
            nopick = dfs(i+1,j)
            dp[(i,j)] = max( pick,nopick)
            return dp[(i,j)]
            
        return dfs(0,1)