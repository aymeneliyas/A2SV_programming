class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        for key,val in Counter(nums).items():
            if val > len(nums) // 3:
                ans.append(key)
        return ans
