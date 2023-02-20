class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        root = floor(c**0.5)
        left = 0
        right = root

        while left <= right:
            product = left**2 + right**2
        
            if product == c:
                return True
            elif product < c:
                left += 1
            elif product > c:
                right -= 1
                
            
        return False
