N= int(input())
for i in range(N):
    ans = ""
    string = input()
    j = 0
    while j < len(string)-1:
        if string[j] == string[j+1]:
            j += 2
            if len(string) - j == 1:
                ans += string[j]
    
        elif string[j] != string[j+1]:
            ans += string[j]
            if j == len(string)-2:
                ans += string[j+1]
            j += 1
    if len(string) == 1:
        ans += string
         
    li = list(set(ans))
    li.sort()
    answer = ""
    for i in li:
        answer += i
    print(answer)
