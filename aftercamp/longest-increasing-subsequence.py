class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def rec(prev,cur):
            if cur >= len(nums):
                return 0
            
            if prev in dp:
                return dp[prev]
            nopick = rec(prev,cur + 1)

            pick = 0
            if prev == - 1 or nums[cur] > nums[prev]:
                pick = 1 + rec(cur,cur + 1)
            
            dp[prev] = max(pick,nopick)
            return dp[prev]
        
        return rec(-1,0)