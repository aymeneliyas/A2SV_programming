class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = num2 = float('inf')
        for i in nums:
            if num1>=i:
                num1=i
            elif num2>=i:
                num2=i
            else:
                return True
        return False