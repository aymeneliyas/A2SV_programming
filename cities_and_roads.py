n = int(input())
count = 0
for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        if arr[j] == 1:
            count += 1
print(count//2)