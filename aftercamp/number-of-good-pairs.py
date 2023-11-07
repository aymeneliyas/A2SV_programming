class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        seen = set()
        ans = 0
        for key,val in counter.items():
            
            ans += val * (val-1) // 2
        
        return ans