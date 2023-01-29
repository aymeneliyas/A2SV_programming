from collections import Counter
rowlen,collen = map(int,input().split())
mat = []
ans = []
for row in range(rowlen):
    arr = input() 
    mat.append(arr)
 
for row in range(rowlen):
    indices = []
    count = Counter(mat[row])
    for col in range(collen):
        if count[mat[row][col]] == 1:
            column = []    
            for j in range(0,rowlen):
                column.append(mat[j][col])
            count2 = Counter(column)
            if count2[mat[row][col]] == 1:
                ans.append(mat[row][col])
print("".join(ans))
