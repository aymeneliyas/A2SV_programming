class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = ceil(total / 2)

        def dfs(i,val):
            if val >= target or i == len(stones):
                return abs(val - (total - val))
            
            if (i,val) in dp:
                return dp[(i,val)]
            

            dp[(i,val)] = min(dfs(i+1,val),dfs(i+1,val+stones[i]))
            return dp[(i,val)]
        dp = {}
        return dfs(0,0)