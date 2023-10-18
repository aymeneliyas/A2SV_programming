class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        mini = min(nums)

        if (maxi - k) -  (mini + k) <= 0:
            return 0
        
        else:
            return (maxi - k) - (mini + k)