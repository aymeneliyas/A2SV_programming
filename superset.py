# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(map(int,input().split()))
n = int(input())
ans = True
for i in range(n):
    setB = set(map(int,input().split()))
    
    for elm in setB:
        if elm not in setA:
            ans = False
        elif len(setA) < len(setB):
            ans = False    
print(ans)
