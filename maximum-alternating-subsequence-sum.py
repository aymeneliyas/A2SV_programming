class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        @cache
        def rec(index,pos):
            if index == len(nums):
                return 0
            
            if pos:
                num = nums[index]
            else:
                num = -nums[index]
            

            pick = num + rec(index+1,not pos)
            nopick = rec(index+1,pos)

            return max(pick,nopick)
        
        return rec(0,True)