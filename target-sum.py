class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def solve(index,total):
            if index == len(nums):
                return 1 if total == target else 0

            if (index,total) in memo:
                return memo[(index,total)]

            memo[(index,total)] = solve(index+1,total + nums[index]) + solve(index+1,total-nums[index])
            return memo[(index,total)]

        return solve(0,0)