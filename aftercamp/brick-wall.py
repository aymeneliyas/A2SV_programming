class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        tot = sum(wall[0])
        big = float("inf")       
        pregrid = []
        dic = defaultdict(int)
        for i in range(len(wall)):
            a = [wall[i][0]]
            big = min(big,len(wall[i])) 
            for j in range(1,len(wall[i])):
                a.append(a[-1] + wall[i][j])
            
            for num in a:
                dic[num] += 1
        
        dic[tot] = 0
        return len(wall) - max(dic.values())

        