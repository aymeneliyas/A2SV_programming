ans = []
n = int(input())
for i in range(n):
    m = int(input())
    arr = list(map(int,input().split()))
    temp = []
    for i in range(m):
        temp = arr[:i] + arr[i+1:]
        val = temp[0]
        for j in range(1,len(temp)):
            val = val ^ temp[j]
        if val == arr[i]:
            print(val)
            break