class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        small = min(nums)
        i = 0
        result = []
        while i < len(nums):
            num = nums[i]-1
            if i != num and nums[num] != nums[i]:
                nums[i],nums[num] = nums[num],nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(nums[i])
        return result