class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def solve(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 1
            
            if i in memo:
                return memo[i]
            memo[i] = solve(i-1) + solve(i-2) + solve(i-3) 
            return memo[i]

        return solve(n)