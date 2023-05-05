from collections import defaultdict
graph = defaultdict(list)
n = int(input())
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(len(arr)):
        if arr[j] == 1:
            graph[i+1].append(j+1)
for key,val in graph.items():
    print(len(val),*val)