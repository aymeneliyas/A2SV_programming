class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        result = []
        while i < len(nums):
            num = nums[i]-1
            if i != num and nums[num] != nums[i]:
                nums[i],nums[num] = nums[num],nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i]-1 != i:
                result.append(nums[i])
                result.append(i+1)
        return result