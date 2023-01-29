N = int(input())
for i in range(N):
    temp = []
    length = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) <= 1:
            temp.append(arr[i])
    if len(arr)-len(temp) == 1 :
        print("yes")
    else:
        print("no")
