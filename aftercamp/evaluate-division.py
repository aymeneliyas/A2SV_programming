class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i,val in enumerate(equations):
            num,den = val
            graph[num].append([den,values[i]])
            graph[den].append([num,1/values[i]])
        
        def dfs(src,target):
            if src not in graph or target not in graph:
                return -1
            queue = deque()
            queue.append([src,1])
            visited = set()
            visited.add(src)
            while queue:
                
                node,w = queue.popleft()
                
                if node == target:
                    return w
                
                for n, weight in graph[node]:
                    if n not in visited:
                        queue.append([n,w*weight])
                        visited.add(n)
            return -1
        return [dfs(src,target) for src,target in queries]