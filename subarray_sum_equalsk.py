class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        dic = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            prefix.append(prefix[-1]+nums[i])
        for fix in prefix:
            if (fix-k) in dic:
                count += dic[fix-k]
            dic[fix] += 1
        return count
