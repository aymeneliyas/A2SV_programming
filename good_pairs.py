class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        len1 = len(nums)
        for i in range(len1):
            for j in range(0,i):
                if nums[i] == nums[j]:
                    ans += 1
        return ans
