from collections import defaultdict
 
N = int(input())
 
for _ in range(N):
	ans = 0
	row,col = map(int,input().split())
	num1 = defaultdict(int)
	num2 = defaultdict(int)
	matrix = []
	for i in range(row):
		matrix.append(list(map(int,input().split())))
 
 
	for i in range(row):
		for j in range(col):
			num1[i+j] += matrix[i][j]
			num2[i-j] += matrix[i][j]
	for i in range(row):
		for j in range(col):
			ans = max(ans,(num1[i+j]+num2[i-j] - matrix[i][j]))
      
	print(ans)