class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if len(graph) == 0:
            return []
        ans = []
        terminal = set()
    
        for idx,val in enumerate(graph):
            if len(val) == 0:
                terminal.add(idx)
        colors = [0] * len(graph)

        def dfs(node,colors):
            if colors[node] == 2:
                return False
            if node in terminal:
                return False

            if colors[node] == 1:
                return True
            
            colors[node] = 1

            for ver in graph[node]:
                cycle_found = dfs(ver,colors)
                if cycle_found:
                    return True
                
            colors[node] = 2
            ans.append(node)
            return False

        for key,node in enumerate(graph):
            cycle_found = dfs(key,colors)
            if not cycle_found:
                ans.append(key)

        val = list(set(ans))
        val.sort()
        return val