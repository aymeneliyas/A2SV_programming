class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        ans = 0
        while n > 0:
            n -= i
            if n >= 0:
                ans += 1
            i += 1
        return ans