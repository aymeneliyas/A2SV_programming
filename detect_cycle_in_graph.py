from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def dfs(self,color,node,parent,adj):
        if color[node] == 2:
            return False
            
        if color[node] == 1:
            return True

        color[node] = 1
        for ver in adj[node]:
            if ver != parent:
                cycle = self.dfs(color,ver,node,adj)
                if cycle:
                    return True
        color[node] = 2
        return False
        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		color = [0] * V
		for i in range(V):
		    cycle = self.dfs(color,i,-1,adj)
		    if cycle:
		        return True
		       
		return False
		