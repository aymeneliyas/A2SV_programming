class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        leader = 0
        self.lead = []
        dic = defaultdict(int)
        for val in self.persons:
            dic[val] += 1
            if dic[leader] <= dic[val]:
                leader = val
            self.lead.append(leader)
        
    def search(self, t):
        left = 0
        right = len(self.times)-1
        ans = -1
        while left <= right:
            mid = left + (right - left)//2
            val = self.times[mid]
            if val == t:
                return mid
            elif val < t:
                ans = max(ans, mid)
                left = mid+1
            else:
                right = mid-1
        # print ans, len(self.times)-1
        return ans

    def q(self, t: int) -> int:
        time = self.search(t)
        # print t_index
        return self.lead[time]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)