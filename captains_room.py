# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
k = input()
room = defaultdict(int)
r = list(map(int, input().split()))

for i in r:
    room[i] += 1

captain = min(room, key = room.get)
print(captain)
