class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        size = len(questions)-1
        memo = {}
        def dp(idx):
            if idx > size:
                return 0
            if idx in memo:
                return memo[idx]

            take = questions[idx][0] + dp(idx + questions[idx][1]+1)
            leave = dp(idx + 1)

            memo[idx] = max(take,leave)
            return memo[idx]
        
        return dp(0)