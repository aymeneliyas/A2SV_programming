class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        edges = defaultdict(int)
        for i,j in prerequisites:
            graph[j].append(i)
            edges[i] += 1
        
        def bfs(queue):
            ans = []
            while queue:
                node = queue.popleft()
                ans.append(node)

                for ver in graph[node]:
                    edges[ver] -= 1
                    if edges[ver] == 0:
                        queue.append(ver)
            
            return ans
        
        queue = deque()
        for i in range(numCourses):
            if edges[i] == 0:
                queue.append(i)
        
        ans = bfs(queue)
        if len(ans) != numCourses:
            return False
        return True