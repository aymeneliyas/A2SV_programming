class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for i in range(n)]
        edge = [0] * n
        
        
        for src,dest in richer:
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
        
        answer = [i for i in range(n)]
        for idx,anc in enumerate(ans):
            mini = answer[idx]
            for node in anc:
                if quiet[node] < quiet[mini]:
                    mini = node
            answer[idx] = mini
        
        return answer