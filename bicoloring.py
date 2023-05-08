from collections import defaultdict
def dfs(vertex,color, graph, visited):
    visited[vertex] = color
    for ver in graph[vertex]:
        if ver not in visited:
            if not dfs(ver, 1-color, graph, visited):
                return False
        elif visited[ver] == color:
            return False
    return True

n = int(input())
while n != 0:
    m = int(input())
    graph = defaultdict(set)
    visited = {}

    for _ in range(m):
        ver1,ver2 = map(int, input().split())
        graph[ver1].add(ver2)
        graph[ver2].add(ver1)

    for node in range(1, n+1):
        if node not in visited:
            if not dfs(node,1,graph, visited):
                print("NOT BICOLOURABLE.")
                break
    else:
        print("BICOLOURABLE.")
    n = int(input())