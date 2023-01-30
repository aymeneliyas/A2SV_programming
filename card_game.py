wube = 0
henok = 0
wubeTurn = True
N = int(input())
arr = list(map(int,input().split()))
left = 0
right = len(arr)-1
 
while left < right:
    if wubeTurn:
        if arr[left] > arr[right]:
            wube += arr[left]
            left += 1
        elif arr[left] <= arr[right]:
            wube += arr[right]
            right -= 1
        wubeTurn = False
        
    else:
        if arr[left] > arr[right]:
            henok += arr[left]
            left += 1
        elif arr[left] <= arr[right]:
            henok += arr[right]
            right -= 1
        wubeTurn = True
if len(arr) %2 == 0:
    henok += arr[left]
else:
    wube += arr[left]
print(wube,henok)
