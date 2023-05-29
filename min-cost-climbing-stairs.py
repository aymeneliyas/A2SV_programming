class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def solve(n):
            if n < 2:
                return cost[n]
            if n in memo:
                return memo[n]
            

            
            val = cost[n] + min(solve(n-1),solve(n-2))
            memo[n] = val
            return val
        return min(solve(len(cost)-1),solve(len(cost)-2))