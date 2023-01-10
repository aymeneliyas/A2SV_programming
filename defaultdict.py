from collections import defaultdict
n,m = list(map(int,input().split()))
arrdict = defaultdict(list)
for i in range(n):
    val = input()
    arrdict[val].append(i + 1)

for i in range(m):
    val = input()
    if arrdict[val]:
        print(*arrdict[val])
    else:
        print(-1)
