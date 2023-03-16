class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        
        while left < right:
            middle = left + (right - left) // 2
            tot = 0
            ans = 1

            for w in weights:
                tot += w
                if tot > middle:
                    ans+=1
                    tot = w
            
            
            if ans > days:
                left = middle+1
            if ans <= days:
                right = middle
    
        return right