class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        small = min(nums)
        i = 0
        while i < len(nums):
            num = nums[i]-1
            if i != num and nums[num] != nums[i]:
                nums[i],nums[num] = nums[num],nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]