class Solution:
    def maxScore(self, nums: List[int]) -> int:
        mask = 0
        @cache
        def rec(mask,n):
            result = 0
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if (mask >> i) & 1 or (mask >> j) & 1:
                        continue
                    mask |= (1 << i)
                    mask |= (1 << j)
                    result = max(result,rec(mask,n+1) + n * gcd(nums[i],nums[j]))
                    mask ^= (1 << i)
                    mask ^= (1 << j)
        
            return result
        
        return rec(mask,1)