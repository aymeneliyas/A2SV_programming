class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i)
        del prefix[0]
        print(prefix)
        ans = 0
        dic = defaultdict(int)
        dic[0] = 1
        for i in prefix:
            if (i-goal) in dic:
                ans += dic[i-goal]
            dic[i] += 1
        return ans