class Solution:
    def getFirst(self,nums,left1,right1,target):
        while left1+1 < right1:
        
            mid = left1 + (right1-left1) // 2
            if nums[mid] < target:
                left1 = mid
            else:
                right1 = mid
        return right1 if right1 != len(nums) and nums[right1] == target else -1  

    def getLast(self,nums,left,right,target):
        while left+1 < right:
        
            mid = left + (right-left) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        return left if left >= 0 and nums[left] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.getFirst(nums,-1,len(nums),target)
        last = self.getLast(nums,-1,len(nums),target)
        
    
        return [first,last]