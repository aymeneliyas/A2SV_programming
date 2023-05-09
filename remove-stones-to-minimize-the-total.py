class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        arr = [-i for i in piles]
        heapq.heapify(arr)
        for i in range(k):
            val = heapq.heappop(arr)
            val1 = abs(val)
            heapq.heappush(arr,-val1//2)
        
        return abs(sum(arr))