class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        incoming = [0] * (numCourses)


        for start,end in prerequisites:
            graph[start].append(end)
            incoming[end] += 1
    
        queue = deque()
        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
    
        dic = defaultdict(set)
        while queue:
            node = queue.popleft()
            for ver in graph[node]:
                dic[ver].add(node)
                dic[ver].update(dic[node])
                incoming[ver] -= 1
                if incoming[ver] == 0:
                    queue.append(ver)

    
        ans = []
        for x,y in queries:
            if x in dic[y]:
                ans.append(True)
            else:
                ans.append(False)

        return ans