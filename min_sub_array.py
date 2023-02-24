class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        window = float('inf')
        tot = 0
        while right < len(nums):
            tot += nums[right]
            
            while tot >= target:
                window = min(window,right - left + 1)
                tot -= nums[left]
                left += 1
            
            right += 1
        if window == float('inf'):
            return 0
        return window
