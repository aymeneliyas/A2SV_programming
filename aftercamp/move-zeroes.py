class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        0 1 0 3 12
        zero = 0
                
        """
        left = 0
        for ind in range(len(nums)):
            if nums[ind] != 0:
                nums[left],nums[ind] = nums[ind],nums[left]
                left += 1
         
         
            