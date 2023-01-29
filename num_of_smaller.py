n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
 
 
left = 0
for i in range(m):
    while left < n and arr1[left] < arr2[i]:
        left += 1
    print(left,end=" ")
