EN = input()
english = set(map(int,input().split()))
FN = input()
french = set(map(int,input().split()))
ans = english.difference(french)

print(len(ans))
