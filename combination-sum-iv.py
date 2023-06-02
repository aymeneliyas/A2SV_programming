class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def solve(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            
            if target in memo:
                return memo[target]
            res = 0
            for i in nums:
                res += solve(target-i)
            
            memo[target] = res
            return res
        
        return solve(target)