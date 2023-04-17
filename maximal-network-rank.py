class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(list)
        for road in roads:
            dic[road[0]].append(road[1])
            dic[road[1]].append(road[0])
            
        max_rank = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                max_rank = max(max_rank, len(dic[i]) +
                              len(dic[j]) - (j in dic[i]))
        return max_rank