class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        def dfs(cur,par):
            time = 0
            for ver in graph[cur]:
                if ver == par:
                    continue
                
                val = dfs(ver,cur)
                if val or hasApple[ver]:
                    time += val + 2
                
            return time
        
        return dfs(0,-1)