class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        ans = []

        for key,val in count.items():
            heappush(heap,(-val,key))

        for i in range(k):
            ans.append(heappop(heap)[1])
        
        return ans