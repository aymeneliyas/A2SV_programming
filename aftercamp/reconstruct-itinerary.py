class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start,end in tickets:
            graph[start].append(end)
        
        for key in graph:
            graph[key].sort(reverse=True)
        
        ans = []
        def dfs(node):
            if node in graph:
                while graph[node]:
                    n = graph[node].pop()
                    dfs(n)
            ans.append(node)
        dfs("JFK")
        return ans[::-1]