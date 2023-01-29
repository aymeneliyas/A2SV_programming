class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        """
        1 3 4 2 3 5 6 10 11 22 0
        """
        i = len(piles)-1
        ans = 0
        
        l = 0
        while l < i-1 and i-2 >= 0:
            arr = piles[i-1 : i+1]
            ans += arr[0]
            
            i -= 2 
            l += 1
        return ans
