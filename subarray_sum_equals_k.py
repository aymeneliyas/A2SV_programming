class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        curSum = 0
        prefixSum = {0:1}
        for a in nums:
            curSum += a
            val = curSum - k
            res += prefixSum.get(val,0)
            prefixSum[curSum] = prefixSum.get(curSum,0) + 1
        return res
