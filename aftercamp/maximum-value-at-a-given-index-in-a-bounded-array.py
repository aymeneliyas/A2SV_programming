class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def getSum(val,index,n):
            ans = 0
            if val > index:
                ans += (val + val - index) * (index + 1)//2
            else:
                ans += (val + 1) * val // 2
                ans += (index - val) + 1

            if val > n - index:
                ans += (val + val - n + 1 + index) * (n - index) // 2
            else:
                ans += (val + 1) * val // 2 + (n - index - val)

            return ans - val
        
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if getSum(mid, index, n) <= maxSum:
                left = mid
            else:
                right = mid - 1
        
        return left