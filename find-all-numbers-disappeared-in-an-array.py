class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        idx = 0
        size = len(nums)
        while idx < size:
            pos = nums[idx]-1
            if nums[idx] == nums[pos] and pos != idx:
                idx += 1
            elif pos != idx:
                nums[pos], nums[idx] = nums[idx], nums[pos]
            else:
                idx += 1

        result = []
        for idx in range(size):
            if nums[idx] != idx +1:
                result.append(idx+1)
        return result