class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            incoming[a] += 1
            incoming[b] += 1
        queue = deque()
        res = []
        for node in graph:
            if incoming[node] == 1: 
                queue.append(node) 
                incoming[node] -= 1
        
        while queue:
            res = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                res.append(node)
                
                for ver in graph[node]:
                    incoming[ver] -= 1
                    if incoming[ver] == 1:
                        queue.append(ver)
        return res if res else [0]