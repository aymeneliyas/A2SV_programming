class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = sorted(count, key=lambda x : count[x])
        
        return sorted_count[-k:]