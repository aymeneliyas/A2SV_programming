class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        while left < len(nums)-1:
            if nums[left] == nums[left+1]:
                nums.pop(left+1)
            else:
                left += 1
        return len(nums)
