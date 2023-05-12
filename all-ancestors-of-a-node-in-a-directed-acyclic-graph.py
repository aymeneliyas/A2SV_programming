class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        edge = [0] * n
        
        
        for src,dest in edges:
            graph[src].append(dest)
            edge[dest] += 1
        
        queue = deque()
        ans = [set() for _ in range(n)]
        
        for i in range(len(edge)):
            if(edge[i] == 0):
                queue.append(i)
        
        while queue:
            cur = queue.pop()
    
            for neighbor in graph[cur]:
                
                ans[neighbor].add(cur)
                ans[neighbor].update(ans[cur])
                edge[neighbor] -= 1
                if(edge[neighbor] == 0):
                    queue.append(neighbor)
        
        ans = [(sorted(list(s))) for s in ans]
        return ans