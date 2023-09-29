n = int(input())
 
for _ in range(n):
    num = int(input())
    val = num
    ans = []
    i = 9
    while num > 0:
        num -= i
 
        if num > 0:
            ans.append(i)
        i -= 1
    ans.append(val-sum(ans))
    ans.sort()
    answer = []
    for i in ans:
        answer += str(i)
    print("".join(answer))