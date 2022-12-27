# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for index in range(T):
    size = int(input())
    array = list(map(int,input().split()))
    i = 0
    j = len(array)-1
    start = 0
    flag = True
    while(i != j):
        
        if array[i] > array[j]:
            start = i
            i+=1
            if start != 0 and array[start] < array[i]:
                flag = False
                break
                
        else:
            start = j
            j-=1
            if start != 0 and array[start] < array[j]:
                flag = False
                break
    if flag:
        print("Yes")
    else:
        print("No")
