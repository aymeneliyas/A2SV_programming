from collections import defaultdict
N = int(input())

for i in range(N):
    planet_len = list(map(int,input().split()))
    
    planets = list(map(int,input().split()))
    
    planet_map = defaultdict(int)
    
    for i in planets:
        planet_map[i] += 1
    ans = 0
    
    for key,val in planet_map.items():
        
        if val > planet_len[1]:
            ans += planet_len[1]
        else:
            ans += val
        
    print(ans)
