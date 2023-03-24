n = int(input())

def merge_sort(left,right,nums,count):
    if left == right:
        return [[nums[left]],0]

    mid = left + (right-left) // 2
    left_half = merge_sort(left,mid,nums,count)
    right_half = merge_sort(mid+1,right,nums,count)
    count , swap = 0,False
    arr = []
    if left_half[0][0] < right_half[0][0]:
        arr = left_half[0] + right_half[0]
    else:
        arr = right_half[0] + left_half[0]
        swap = True
    if swap == True:
        count = 1
    return [arr,count + left_half[1]+right_half[1]]      


for i in range(n):
    leng = int(input())
    arr = list(map(int,input().split()))
    level = 0
    r = len(arr)-1
    l = 0
    ans,count = merge_sort(l,r,arr,0)
    s = sorted(arr)
    if s == ans:
        print(count)
    else:
        print(-1)
