class Solution:
    def mySqrt(self, x: int) -> int:
        left = -1
        right = (x//2)+1
        if x == 1:
            return 1
        while left+1 < right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid 
            else:
                right = mid  
        return left