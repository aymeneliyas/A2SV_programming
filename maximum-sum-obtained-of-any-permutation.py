class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        arr = [0] * (len(nums)+1)
        for req in requests:
            arr[req[0]] += 1
            arr[req[1]+1] -= 1
        
        prefix = [0]
        for i in range(len(arr)):
            prefix.append(prefix[-1] + arr[i])
        prefix.sort(reverse=True)
        res = 0

        for i in range(len(nums)):
            if prefix[i] == 0:
                break
        
            res += (prefix[i] * nums[i])
        
        return res % (10**9 + 7)