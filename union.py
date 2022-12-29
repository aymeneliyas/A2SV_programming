# Enter your code here. Read input from STDIN. Print output to STDOUT
EN = input()
english = set(map(int,input().split()))
FN = input()
french = set(map(int,input().split()))

ans = french.union(english)
print(len(ans))
