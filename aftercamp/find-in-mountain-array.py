# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        low = 0
        high = length-1

        while low < high:
            mid = low + (high-low)//2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                low = mid + 1
            else:
                high = mid
        
        peak = low

        low = 0
        high = peak

        while low < high:
            mid = low + (high - low) // 2
            if mountain_arr.get(mid) < target:
                low = mid + 1
            else:
                high = mid
        
        if mountain_arr.get(low) == target:
            return low
        
        low = peak
        high = length-1
        while low < high:
            mid = low + (high-low) // 2
            if mountain_arr.get(mid) > target:
                low = mid + 1
            else:
                high = mid
        
        if mountain_arr.get(high) == target:
            return high
        else:
            return -1