from collections import defaultdict,deque
def parallelCourses(n, prerequisites):
    # Write your code 
    graph = defaultdict(list)
    incoming = [0] * (n+1) 

    visited = set()

    for a,b in prerequisites:
        graph[a].append(b)
        incoming[b] += 1
    
    queue = deque()
    for i in range(1,n+1):
        if incoming[i] == 0:
            queue.append(i)
            visited.add(i)
    
    answer = 0
    while queue:
        l = len(queue)
        
        for _ in range(l):
            node = queue.popleft()
            for ver in graph[node]:
                if ver not in visited:
                    incoming[ver] -= 1
                    if incoming[ver] == 0:
                        queue.append(ver)
                        visited.add(ver)
        answer += 1
    if len(visited) == n:
        return answer
    return -1

