n = int(input())

for _ in range(n):
    prog , math = map(int,input().split())
    ans = min(prog, math , (prog + math)//4)
    print(ans)