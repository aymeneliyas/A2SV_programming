class Solution(object):
    def moveZeroes(self, nums):
        """
        [0,1,0,3,12]
        l = 0 r =1
        [1,0,0,3,12]
        l=1,r=2
        l=2,r=3
        
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
