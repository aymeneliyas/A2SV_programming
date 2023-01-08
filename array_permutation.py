class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []
        for i in range(length):
            ans.append(nums[nums[i]])

        return ans
