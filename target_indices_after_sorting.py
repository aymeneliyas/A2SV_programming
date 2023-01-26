class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        for idx in range(len(nums)):
            if nums[idx] == target:
                ans.append(idx)
        return ans
