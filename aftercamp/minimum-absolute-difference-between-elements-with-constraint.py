from sortedcontainers import SortedSet
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        arr = SortedSet()
        ans = inf

        for key,val in enumerate(nums):
            if key - x >= 0:
                arr.add(nums[key-x])
            
            
            if arr:
                right = min(bisect_right(arr,val),len(arr)-1)
                left = max(right-1,0)
                ans = min(ans,abs(val-arr[right]),abs(val-arr[left]))
            
        return ans
