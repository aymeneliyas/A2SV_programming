class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] =1
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        dic = defaultdict(int)
        count = 0
        for val in prefix:
            if (val-k) in dic:
                count += dic[val-k]
            dic[val] += 1
        return count