n = int(input())
mat = []
sources = []
sinks = []

for i in range(n):
    arr = list(map(int,input().split()))
    if 1 not in arr:
        sinks.append(i+1)
    mat.append(arr)

for row in range(len(mat)):
    i = 0
    for col in range(len(mat[0])):
        if mat[col][row] == 1:
            i += 1
    if i == 0:
        sources.append(row+1)


print(len(sources), *sources)
print(len(sinks), *sinks)