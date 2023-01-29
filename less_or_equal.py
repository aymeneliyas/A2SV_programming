inp = list(map(int,input().split()))
arr = list(map(int,input().split()))
k = inp[1]
arr.sort()
num = arr[k-1]+1
count = 0
if k ==0:
    minimum = min(arr)
    if minimum-1 != 0:
        print(minimum-1)
    else:
        print(-1)
else:
    for i in range(inp[0]):
        if num > arr[i]:
            count += 1
    if count == k:
        print(arr[k-1])
    else:
        print(-1)
