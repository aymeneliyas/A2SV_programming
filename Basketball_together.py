n,d = list(map(int,input().split()))
powers = list(map(int,input().split()))
powers.sort()
ans = 0
left = 0
right = len(powers)-1
while left < right:
    count = powers[right]
    while left < right and count <= d:
        count += powers[right]
        left += 1
    if count > d:
        ans += 1
    right -= 1
if powers[left] > d:
    ans += 1
if len(powers) == 1:
    if powers[0] > d:
        print(1)
    else:
        print(0)
else:
    print(ans)