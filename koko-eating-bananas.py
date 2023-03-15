class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left+1 < right:
            middle = left + (right - left) // 2
            value = 0
            for i in piles:
                value += math.ceil(i/middle)
            
            if value <= h:
                right = middle
            elif value > h:
                left = middle
        if left == 1:
            if sum(piles) <= h:
                return 1 
        return right