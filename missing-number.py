class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        if len(nums) not in nums:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] != i:
                return i