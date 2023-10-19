class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        nums.sort()

        s = sum(nums)

        if s%2 == 1:
            return False
            
        memo = {}

        def helper(start_index, target):

            if (start_index, target) in memo:
                return memo[(start_index, target)]

            if start_index >= l:
                return False

            if target == 0:
                return True

            if nums[start_index] <= target:
                memo[(start_index, target)] = helper(start_index+1, target-nums[start_index]) or helper(start_index+1, target)
                return memo[(start_index, target)]
            else:
                return False
        
        return helper(0, s / 2)