class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        ans = 0
        val = nums[0]
        val1 = nums[0]
        for num in nums:
            val1 &= num
        if val1 != 0:
            return 1
        
        for i in range(len(nums)):
            val &= nums[i]

            if val == 0:
                ans += 1
                if i+1 < len(nums):
                    val = nums[i+1]

        return ans