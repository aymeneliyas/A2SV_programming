class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        first = dict()
        last = dict()
        deg = max(count.values())
        for key,val in enumerate(nums):
            if val not in first:
                first[val] = key
            last[val] = key

        
        ans = float('inf')
        for key,val in count.items():
            if val == deg:
                ans = min(ans,(last[key]-first[key])+1)
        
        return ans