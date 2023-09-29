from collections import Counter
n = int(input())
for _ in range(n):
    planets , mach2 = list(map(int,input().split()))
    arr = list(map(int,input().split()))
 
    count = Counter(arr)
    ans = 0
    for key,val in count.items():
        if val > mach2:
            ans += mach2
        else:
            ans += val
    print(ans)