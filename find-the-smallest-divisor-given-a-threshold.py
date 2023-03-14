class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 0
        right = max(nums)

        while left < right:
            middle = left + (right - left)//2
            total = 0
            for i in nums:
                total += math.ceil(i/middle)
            if total > threshold:
                left = middle+1
            else:
                right = middle 
        return left