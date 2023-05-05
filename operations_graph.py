from collections import defaultdict
vertices = int(input())
n = int(input())

graph = defaultdict(list)
for _ in range(n):
    nums = list(map(int,input().split()))
    if nums[0] == 1:
        graph[nums[1]].append(nums[2])
        graph[nums[2]].append(nums[1])
    else:
        print(*graph[nums[1]])