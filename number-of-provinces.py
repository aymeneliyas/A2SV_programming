class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        def dfs(isConnected, visited, node):
            if node in visited:
                return 0
            visited.add(node)  
            for j in range(len(isConnected[node])):
                if isConnected[node][j] == 1:
                    dfs(isConnected, visited, j)  
            return 1 
        
        provinces = 0  
        for i in range(len(isConnected)):  
            provinces += dfs(isConnected, visited, i) 
        return provinces