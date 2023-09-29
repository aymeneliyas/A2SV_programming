from collections import defaultdict
n = int(input())
graph = defaultdict(list)
for i in range(n):
    arr = list(map(str,input().split()))
    graph[arr[2].upper()].append(arr[0].upper())
 
visited = set()
def dfs(node, depth=1):
    global maxdepth
    maxdepth = max(depth,maxdepth)
    if node not in visited:
        visited.add(node)
        for child in graph[node]:
            dfs(child,depth+1)
        
maxdepth = 1
dfs("POLYCARP")
print(maxdepth)